
#from flask import render_template, request
from flask_socketio import SocketIO
from webserver import socketio
from webserver import mon_robot
import json

@socketio.on('my event')
def handle_my_custom_event(commande_json, methods=['GET', 'POST']):
    #print('received my event: ' + str(commande_json))

    Y = int(commande_json['Y']) / 110
    X = int(commande_json['X']) / 110

    if abs(X) <= abs(Y)  :
        if X > 0:
            D = Y - X 
            G = Y 
        else:
            D = Y 
            G = Y + X 
    elif abs(X) > abs(Y) :
            D = -X 
            G = X  
    else:
        D = 0
        G = 0
    

    """
    if D > 0:
        D = D * 0.6 + 0.4
    elif D < 0:
        D = D * 0.6 - 0.4

    if G > 0:
        G = G * 0.6 + 0.4
    elif G < 0:
        G = G * 0.6 - 0.4
    """

    #print('Commande moteur D G : ' + str(D) + " " + str(G))

    mon_robot.set_ordre_moteur(D, G)