
#from flask import render_template, request
from flask_socketio import SocketIO
from webserver import socketio

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))