from AppContext import AppContext
from libs.microdot.microdot import Microdot

app = Microdot()
context : AppContext = None # type: ignore

@app.route('/')
async def index(request):
    return 'Hello, world!'

@app.route('/set/<value>')
async def ddd(request, value):
    print(f"temp set to {value}")
    context.required_temperature = value
    return context.required_temperature

@app.post('/')
async def new_customer(request):
    print("SOME POST")
    return 'Hi friend!'

def get_endpoints(appContext : AppContext):
    global context 
    context = appContext
    return app