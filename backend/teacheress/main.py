from fastapi import FastAPI
from teacheress.controller.user import UserController
from teacheress.controller.appointment import Appointment
from teacheress.controller.routing import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
