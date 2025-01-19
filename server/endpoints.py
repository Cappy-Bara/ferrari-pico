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
    message = "required temperature set to: " + value
    print(message)
    context.required_temperature = int(value)
    return message

@app.post('/heater/<id>/switch')
async def switch_heater_state(request, id):

    if(id == "up"):
        context.up_heater_plugged = not context.up_heater_plugged
        message = f'Up heater set to : {context.up_heater_plugged}'

    elif(id == "down"):
        context.down_heater_plugged = not context.down_heater_plugged
        message = f'Down heater set to : {context.up_heater_plugged}'
    
    print(message)
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