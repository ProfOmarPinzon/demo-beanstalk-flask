from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Flask funcionando en Elastic Beanstalk"

@application.route("/health")
def health():
    return {"status": "ok"}