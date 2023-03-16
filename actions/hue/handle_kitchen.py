# ---- Philips Hue Api ----
# Getting started: https://developers.meethue.com/develop/get-started-2/ 
# Verify current Ip-address of Hue Bridge in the app settings (or adjust if needed).
# Info: Maybe turn off DHCP in order to not need to switch or set up a DNS
# Get all lights: GET https://192.168.x.y/api/[USER]/lights
# Get specfic light: GET https://192.168.x.y/api/[USER]/lights/{id}
# Set specfic light state: PUT https://192.168.x.y/api/[USER]/lights/{id}/state

from secrets import secrets
import urequests

# From https://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python
def handle_kitchen_toggle():
    headers = { 'Content-Type': 'application/json' }
    hue_ip = secrets['hue_ip']
    hue_user = secrets['hue_user']
    hue_kitchen_id = '4' # TODO: find by name
    
    hue_get_kitchen_url = hue_ip + '/api/' + hue_user + '/lights/' + hue_kitchen_id
    hue_set_kitchen_url = hue_ip + '/api/' + hue_user + '/lights/' + hue_kitchen_id +'/state'

    # Make a put request
    try:
        kitchen_res = urequests.get(hue_get_kitchen_url, headers = headers).json()
    except ValueError:
        print('Error: Response body is not valid JSON')
        
    print('Response of kitchen state', kitchen_res['state'])
    if kitchen_res['state']['on'] == False:
        try:
            urequests.put(hue_set_kitchen_url, headers = headers, data = '{"on": true}')
            print('--> Turning kitchen on!')
        except Exception as e:
            print('Error when turning on kitchen light.', str(e))
    else:
        try:
            urequests.put(hue_set_kitchen_url, headers = headers, data = '{"on": false}')
            print('--> Turning kitchen off!')
        except Exception as e:
            print('Error when turning off kitchen light.', str(e))
