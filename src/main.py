from fastapi import FastAPI
from routes import users, assets, companies, units
from core.models_web import user

app = FastAPI()

app.include_router(users.router)
app.include_router(assets.router)
app.include_router(companies.router)
app.include_router(units.router)

@app.post("/login")
async def login(login: user.Login):
    return {"message": "Login"}
