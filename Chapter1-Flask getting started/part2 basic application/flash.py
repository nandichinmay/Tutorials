from flask import Flask,render_template
from model import db

application=Flask(__name__)

@application.route("/")
def welcome():
    return render_template("hello.html", message="jinja variable")

@application.route("/card")
def card():
    card=db[0]
    return render_template("welcome.html",card=card)

if __name__=="__main__":
    application.run()