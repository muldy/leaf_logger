import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_request_logger import RequestLogger
import sqlalchemy

path ="access.log"

logger = logging.getLogger('werkzeug')
handler = TimedRotatingFileHandler(path, when="midnight")
logger.addHandler(handler)

app = Flask('leaf logger')
req_logger = RequestLogger(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'leaf logger'

