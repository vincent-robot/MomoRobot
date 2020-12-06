from flask import Flask

webserver = Flask(__name__)
webserver.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

webserver.logger.info('first test message...')

from webserver import routes   