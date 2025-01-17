from AppContext import AppContext
from libs.microdot.microdot import Microdot, send_file

home = Microdot()
context : AppContext = None # type: ignore

@home.route('/')
async def index(request):
    return send_file('/server/home.html')