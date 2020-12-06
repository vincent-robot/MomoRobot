from flask import render_template, request
from webserver import webserver
from datetime import datetime


@webserver.route('/')
def hello():
    return 'Hello, World!'

@webserver.route('/manual',methods=['GET'] )
def manual():
    return render_template('manual.html', date_du_jour = str(datetime.now()))
