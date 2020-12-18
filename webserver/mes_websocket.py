
#from flask import render_template, request
from flask_socketio import SocketIO
from webserver import socketio
from webserver import mon_robot
import json

@socketio.on('my event')
def handle_my_custom_event(commande_json, methods=['GET', 'POST']):
    #print('[websocket] - received my event: ' + str(commande_json))

    Y = int(commande_json['Y']) / 1.10
    X = int(commande_json['X']) / 1.10

    if X != 0:
        print('[websocket] - received my event: ' + str(commande_json))
    
    mon_robot.vector_to_differential(X, Y)
    

    
    