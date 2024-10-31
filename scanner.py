#! /bin/python3

import sys # For cmd line arguements
import socket 
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    # Find the target IP address
    target = socket.gethostbyname(sys.argv[1]) # Translate host name to IPV4
else:
    print('Invalid amount of arguements.')
    print('Syntax: python3 scanner.py <ip>')
    sys.exit()
    

# Add a pretty banner
print('-'*50)
print(f'Scanning target {target}')
print(f'Date started: {str(datetime.now())}')
print('-'*50)


try:
    for port in range(50, 3000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # is a float
        result = s.connect_ex((target, port)) # Returns error indicator
        print(f'Checking port {port} -> {result}')
        if result == 0:
            print(f'Port {port} is open')
        s.close()
except KeyboardInterrupt:
    print('\nExiting program.')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()
except socket.error:
    print('Couldn\'t connect to server')
    sys.exit()
