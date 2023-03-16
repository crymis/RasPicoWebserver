from wifi import connect_to_wifi
from webserver import start_webserver

ip = connect_to_wifi()
start_webserver(ip)
