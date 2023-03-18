# Script of https://www.elektronik-kompendium.de/sites/raspberry-pi/2707131.htm

import socket
from router import handle_path

def start_webserver(ip):
    # HTML
    html = """<!DOCTYPE HTML>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="https://upload.wikimedia.org/wikipedia/de/thumb/c/cb/Raspberry_Pi_Logo.svg/800px-Raspberry_Pi_Logo.svg.png">
    <title>Raspberry Pi Pico</title>
    </head>
    
    <body>
    <h1 align="center">Raspberry Pi Pico W</h1>
    <p align="center">Verbindung mit %s</p>
    
    <pre align="center">Made with ❤ by Dan © 2023</pre>
    </body>
    </html>"""

    # Start HTTP-Server
    print('Start Server')
    
    # Define the IP address and port to listen on
    IP_ADDRESS = '0.0.0.0'
    PORT = 80
    
    # Start the server on the Raspberry itself on port
    server_address = socket.getaddrinfo(IP_ADDRESS, PORT)[0][-1]
    server_connection = None
    
    # Create a TCP/IP socket
    server = socket.socket()
    server.bind(server_address)
    server.listen(1)
    print('Server is listening on', str(ip) + ":" + str(PORT))
    print()
    print('Quit with STRG + C')
    print()

    # Listening to incoming requests
    while True:
        try:
            # Wait for a connection
            connection, client_address = server.accept()
            server_connection = connection
            print('HTTP-Request von Client', client_address)
            # Receive the HTTP request and get path from it
            request = connection.recv(1024)
            request_str = str(request, 'utf-8')
            path = request_str.split()[1] # split incoming request by whitespace. Example: GET /blink/1 HTTP/1.1 ...
            print(f'Requested path: {path}')
            
            # send back HTTP-Response as HTML
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
            html_content = html % str(client_address)
            response += html_content
            connection.sendall(response.encode())
            print()
            print('HTTP-HTML-Response sent.')
            print()
            connection.close()
            
            # Router to handle different paths
            handle_path(path)
    
        except OSError as e:
           break
        except (KeyboardInterrupt):
            break
        except Exception as e:
            break
        
    # Close the connection
    try:
        server_connection.close()
        print('Socket connection closed.')
    except NameError:
        print('NameError')
        pass
    server.close()
    print('Server stopped!')

