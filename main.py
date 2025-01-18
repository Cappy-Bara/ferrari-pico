import asyncio
from AppContext import AppContext
from device.states.StateMachine import StateResult
import json
from device.device import handle_device
from server.webserver import run_web_server

class Appsettings:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, Appsettings(**value))
            else:
                setattr(self, key, value)

async def main():
    
    with open('appsettings.json') as f:
        appSettings = Appsettings(**json.load(f))

    appContext = AppContext(appSettings.init_temp, appSettings.is_up_heater_on, appSettings.is_down_heater_on) #type: ignore
    currentState = StateResult(appSettings.init_temp,0,True,True) # type: ignore

    web_server_task = asyncio.create_task(run_web_server(appContext, appSettings.serverSettings, currentState)) # type: ignore
    io_task_task = asyncio.create_task(handle_device(appContext,currentState))
    await asyncio.gather(web_server_task, io_task_task)

asyncio.run(main())