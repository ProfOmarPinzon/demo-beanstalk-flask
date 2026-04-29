from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Flask funcionando en Elastic Beanstalk - version 3"

@application.route("/health")
def health():
    return {"status": "ok"}