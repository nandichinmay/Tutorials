from flask import Flask,render_template,abort,jsonify
from model import db


application=Flask(__name__)

@application.route("/")
def welcome():
    return render_template("hello.html", message="jinja variable",cards=db)

@application.route("/card/<int:index>")
def card(index):
    try:
        card=db[index]
        return render_template("welcome.html",card=card,index=index,max_index=len(db)-1)
    except IndexError:
        abort(404)

@application.route("/api/card/")
def apiCards():
    return jsonify(db)

@application.route("/api/card/<int:index>")
def apiCard(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


if __name__=="__main__":
    application.run()