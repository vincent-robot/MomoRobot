import eventlet
from flask import Flask
from flask_socketio import SocketIO

import robot


webserver = Flask(__name__)
webserver.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
webserver.config['SECRET_KEY'] = 'MomoSecret!'

socketio = SocketIO(webserver)

mon_robot = robot.Robot()

from webserver import routes   
from webserver import mes_websocket




socketio.run(webserver, port=5000,host='0.0.0.0',debug=True)



webserver.logger.info('Arret des moteur et sortie')
mon_robot.set_ordre_moteur(0,0)

