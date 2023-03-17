# ---- ROUTER for incoming requests based on path ----
# Takes incoming request and checks whether a path fits to take a specific action

from actions.hue.handle_kitchen import handle_kitchen_toggle
from actions.hardware.blink import let_blink

def handle_path(request):
    # handles the different paths to the server
    if request.startswith('GET /toggle/kitchen'):
        handle_kitchen_toggle()
    if request.startswith('GET /blink'):
        last_part = request.split('/',3)[2] # request looks like 'GET /blink/123 HTTP/...'
        duration_string = last_part.split(' ', 1)[0] # last_part should look like '123 HTTP/...'
        duration = 0
        try:
            duration = int(duration_string)
        except ValueError:
            pass
        if duration > 0:
            let_blink(duration)
        else:
            let_blink(8)
    else:
        print('There is nothing to do here')

