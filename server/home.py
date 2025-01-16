from AppContext import AppContext
from libs.microdot.microdot import Microdot

home = Microdot()
context : AppContext = None # type: ignore

@home.route('/')
async def index(request):
    return 'Hello, world!'