"""
This script runs the jaddispainting application using a development server.
"""

from os import environ
import socket
from jaddispainting import app

ip = socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', ip)
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
