from AppContext import AppContext
from libs.microdot.microdot import Microdot

app = Microdot()
context : AppContext = None # type: ignore

@app.post('/temperature/<value>')
async def change_temperature(request, value):
    message = "temperature set to: " + value
    print(message)
    context.required_temperature = value
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

def get_endpoints(appContext : AppContext):
    global context 
    context = appContext
    return app