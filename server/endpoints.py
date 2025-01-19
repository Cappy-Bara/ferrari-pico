import asyncio
from AppContext import AppContext
from device.states.StateMachine import StateResult
from libs.microdot.microdot import Microdot
from libs.microdot.sse import with_sse
import json

app = Microdot()
context : AppContext = None # type: ignore
currentState : StateResult = None # type: ignore

@app.post('/temperature/<value>')
async def change_temperature(request, value):
    message = "temperature set to: " + value
    print(message)
    context.required_temperature = int(value)
    return message

@app.post('/heater/<id>/<state>')
async def ddd(request, id, state):
    message = "Heater " + id + " set to : " + state
    print(message)
    
    parsed = True if state == "True" else False
    print(parsed)

    if(id == "up"):
        context.up_heater_plugged = parsed
    elif(id == "down"):
        context.down_heater_plugged = parsed

    return(message)

@app.route('/status')
@with_sse
async def events(request, sse):
    while(True):
        await asyncio.sleep(1)
        result = currentState.__dict__.copy()
        result['top_heater_plugged'] = context.up_heater_plugged 
        result['down_heater_plugged'] = context.down_heater_plugged 
        await sse.send(json.dumps(result))

def get_endpoints(appContext : AppContext, state : StateResult):
    global context, currentState
    context = appContext
    currentState = state 
    return app