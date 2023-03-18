# ---- ROUTER for incoming requests based on path ----
# Takes incoming request and checks whether a path fits to take a specific action

from actions.hue.handle_kitchen import handle_kitchen_toggle
from actions.hardware.blink import let_blink

def handle_path(path):
    # handles the different paths to the server
    if path.startswith('/toggle/kitchen'):
        handle_kitchen_toggle()
        
    elif path.startswith('/blink'):
        duration = 0
        try:
            duration_string = path.split('/')[2] # path looks like '/blink/123'
            duration = int(duration_string)
        except ValueError:
            pass
        except Exception as e:
            pass
        if duration > 0:
            let_blink(duration)
        else:
            let_blink(8)
    else:
        print(f'No matching path found for "{path}"')
