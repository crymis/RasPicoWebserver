# ---- ROUTER for incoming requests based on path ----
# Takes incoming request and checks whether a path fits to take a specific action

from actions.hue.handle_kitchen import handle_kitchen_toggle
from actions.hardware.blink import let_blink

def handle_path(request):
    # handles the different paths to the server
    if request.startswith('GET /toggle/kitchen'):
        handle_kitchen_toggle()
    if request.startswith('GET /blink'):
        let_blink(8)
