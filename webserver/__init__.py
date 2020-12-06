from flask import Flask

webserver = Flask(__name__)

webserver.logger.info('first test message...')

from webserver import routes   