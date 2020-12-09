import eventlet
from flask import Flask
from flask_socketio import SocketIO


webserver = Flask(__name__)
webserver.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
webserver.config['SECRET_KEY'] = 'MomoSecret!'

socketio = SocketIO(webserver)

from webserver import routes   
from webserver import mes_websocket


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))

socketio.run(webserver, port=5000,host='0.0.0.0',debug=True)



webserver.logger.info('first test message...')

