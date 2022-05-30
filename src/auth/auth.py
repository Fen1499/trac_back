from jose import JWTError, jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(st: str):
    return pwd_context.hash(st)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)