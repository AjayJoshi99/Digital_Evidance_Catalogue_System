from flask import render_template, request, Blueprint, session
from pymongo import MongoClient

logout_blueprint = Blueprint("logout", __name__)

@logout_blueprint.route("/logout", methods = ["POST"])
def Logout():
    username = session.get('username') 
    session.pop(username, None)
    return render_template("Login.html")

