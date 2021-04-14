from flask import Flask
from datetime import datetime

application=Flask(__name__)

@application.route("/")
def welcome():
    return "Welcome to my application"

@application.route("/date")
def todate():
    return "Current time is "+ str(datetime.now())

count=0
@application.route("/views")
def viewcount():
    global count
    count=count+1
    return "Number of viewer "+ str(count)

if __name__=="__main__":
    application.url_map
    application.run()