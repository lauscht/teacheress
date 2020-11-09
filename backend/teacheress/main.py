import sys
from fastapi import FastAPI
from teacheress.controller.user import UserController
from teacheress.controller.appointment import Appointment
from teacheress.controller.routing import router

app = FastAPI()
app.include_router(router)


version = f"{sys.version_info.major}.{sys.version_info.minor}"

@app.get("/")
async def root():
    message = f"Hello. I'm running uvicorn in py{version}."
    return {"message": message}

