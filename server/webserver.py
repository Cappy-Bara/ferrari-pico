from AppContext import AppContext
from .endpoints import get_endpoints
from .home import home
from libs.microdot.microdot import Microdot
import network
import asyncio

async def connect_to_network(ssid, pw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pw)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        await asyncio.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

async def run_web_server(appContext : AppContext, serverSettings):
    ip = await connect_to_network(serverSettings.wlan_ssid, serverSettings.wlan_passwd)
    print(f"Starting web server on {ip}:{serverSettings.port}")

    endpoints = get_endpoints(appContext)
    app = Microdot()

    app.mount(home,"/")
    app.mount(endpoints,"/api")

    await app.start_server(host=ip, port=serverSettings.port)


