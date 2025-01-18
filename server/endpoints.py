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
            
    if(id == "up"):
        context.up_heater_plugged = state
    elif(id == "down"):
        context.down_heater_plugged = state

    return(message)

@app.route('/status')
@with_sse
async def events(request, sse):
    while(True):
        await asyncio.sleep(1)
        await sse.send(json.dumps(currentState.__dict__))

def get_endpoints(appContext : AppContext, state : StateResult):
    global context, currentState
    context = appContext
    currentState = state 
    return app