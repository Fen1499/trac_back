from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.models_web import user, company, unit, asset

#EXTREMELY UNSAFE, ONLY FOR SAMPLE PURPOSES
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/trac"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def exec(query: str):
    with engine.connect() as conn:
        result = conn.execute(query)
        return result

###USER###
def create_user(user: user.Create):

    #UNSAFE, DON'T DO THIS IN A REAL SCENARIO, VALID FOR ALL OTHER QUERIES
    #MUCH EASIER THROUGH RAW QUERY
    query = f'''
        INSERT INTO users ("email", "name", "password", "username", "company_id")
        VALUES('{user.email}', '{user.name}', '{user.password}', '{user.username}', {user.company_id})
        RETURNING *;
    '''
    return exec(query).fetchone()

def get_user(id):
    return exec(f'''SELECT * FROM users WHERE id = {id}''').first()

def get_users_by_company(id):
    return exec(f'''SELECT * FROM users WHERE company_id = {id}''').all()

def edit_user(id, user:user.Edit):
    query = f'''
        UPDATE users SET "password" = '{user.password}' WHERE id = {id}
        RETURNING *;
    '''
    return exec(query).fetchone()

def delete_user(id):
    query = f'''
        DELETE FROM users WHERE id = {id}
        RETURNING *;
    '''
    return exec(query).fetchone()
    

###COMPANY###

def get_companies():
    return exec("SELECT * from companies").all()

def get_company(id):
    return exec(f'''SELECT * from companies WHERE id = {id}''').first()

def create_company(company: company.Create):
    query = f'''
        INSERT INTO companies ("name") VALUES ('{company.name}')
        RETURNING *;
    '''

    return exec(query).fetchone()

###UNIT###

def get_units_by_company(id):
    return exec(f'''SELECT * FROM units WHERE company_id = {id}''').all()

def get_unit(id):
        return exec(f'''SELECT * FROM units WHERE id = {id}''').first()

def create_unit(unit: unit.Create):
    query = f'''
        INSERT INTO units ("name", "company_id") VALUES ('{unit.name}', {unit.company_id})
        RETURNING *;
    '''

    return exec(query).fetchone()


###ASSETS###

def get_assets_by_owner(id):
    return exec(f'''SELECT * FROM assets WHERE owner = {id}''').all()

def get_asset(id):
    return exec(f'''SELECT * FROM assets WHERE id = {id}''').first()

def create_asset(asset: asset.Create):
    query = f'''
        INSERT INTO assets ("name", "description", "model", "status", "health_level", "owner")
        VALUES('{asset.name}', '{asset.description}', '{asset.model}', '{asset.status}', {asset.health_level}, {asset.owner})
        RETURNING *    
        '''

    return exec(query).fetchone()






