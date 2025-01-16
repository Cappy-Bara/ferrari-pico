import asyncio
from AppContext import AppContext
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

    appContext = AppContext(500)
    web_server_task = asyncio.create_task(run_web_server(appContext,appSettings.serverSettings)) # type: ignore
    io_task_task = asyncio.create_task(handle_device(appContext))
    await asyncio.gather(web_server_task, io_task_task)

asyncio.run(main())