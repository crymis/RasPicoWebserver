# ---- ROUTER for incoming requests based on path ----
# Takes incoming request and checks whether a path fits to take a specific action

from actions.hue.handle_kitchen import handle_kitchen_toggle
from actions.hardware.blink import let_blink

def handle_path(request):
    # handles the different paths to the server
    if request.startswith('GET /toggle/kitchen'):
        handle_kitchen_toggle()
    if request.startswith('GET /blink'):
        last_slash_position = request.rfind('/')
        if last_slash_position == -1:
            last_slash_position = request.find('/')
        duration_string = request[request[last_slash_position] + 1:]
        duration = int(duration_string)
        print('duration from path', str(duration))
        if duration:
            let_blink(duration)
        else:
            let_blink(8)
