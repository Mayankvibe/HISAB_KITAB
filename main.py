from fastapi import FastAPI
from routes import auth,base_dashboard
from fastapi.staticfiles import StaticFiles
import model
from database import engine
app=FastAPI()

model.Base.metadata.create_all(
    bind=engine
)

app.include_router(auth.routes,prefix="/auth")
app.include_router(base_dashboard.routes,prefix="/base_dashboard")
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)