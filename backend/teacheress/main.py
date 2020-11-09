import sys
from fastapi import FastAPI
import fastapi_plugins as fap
from teacheress.controller.user import UserController
from teacheress.controller.appointment import Appointment
from teacheress.controller.routing import router


class AppSettings(fap.RedisSettings, fap.SchedulerSettings):
    api_name: str = str(__name__)

app = FastAPI()
app.include_router(router)
config = AppSettings()


version = f"{sys.version_info.major}.{sys.version_info.minor}"

@app.get("/")
async def root():
    message = f"Hello. I'm running uvicorn in py{version}."
    return {"message": message}


@app.on_event('startup')
async def on_startup() -> None:
    await fap.redis_plugin.init_app(app, config=config)
    await fap.redis_plugin.init()
    await fap.scheduler_plugin.init_app(app=app, config=config)
    await fap.scheduler_plugin.init()

@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fap.scheduler_plugin.terminate()
    await fap.redis_plugin.terminate()
