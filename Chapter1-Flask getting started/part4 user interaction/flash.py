from flask import Flask,render_template,abort,jsonify,request,url_for,redirect
from model import db,save_db


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

@application.route("/addCard",methods=["GET","POST"])
def addcard():
    if request.method=="POST":
        card={ "name":request.form["name"],
                "class":int(request.form["class"])}
        db.append(card)
        save_db()
        return redirect(url_for('card',index=len(db)-1))
    else:
        return render_template("addcard.html")

@application.route("/removeCard/<int:index>",methods=["GET","POST"])
def removecard(index):
    if request.method=="POST":
        del db[index]
        save_db()
        return redirect(url_for("welcome"))
    else:
        return render_template("removecard.html",card=db[index])



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