from flask import render_template, request, Blueprint, session, flash, redirect, url_for
from pymongo import MongoClient

client = MongoClient("mongodb+srv://ajayjoshi1908:oY3CJK3VDbJ1V0IK@decscluster.gw3pd.mongodb.net/user?retryWrites=true&w=majority")
db = client['user']


add_crime_blueprint = Blueprint("crime", __name__)
add_user_crime_blueprint = Blueprint("useCrime", __name__)
add_user_blueprint = Blueprint("user", __name__)
delete_user_blueprint = Blueprint("deleteUser", __name__)

@add_user_crime_blueprint.route("/addUserCrime", methods = ["POST"] )
def AddUserCrime():
    crime = request.form.get("crime")
    username = request.form.get("username")
    collection = db['user_crime']
    user = db['login'].find_one({"username":username})
    if not user : 
        flash("User does not exists", "danger")
        return render_template("admin.html")
    exist = collection.find_one({"username":username, "crime": crime})
    if exist :
        flash("Data already exists", "danger")
        render_template("admin.html")
    flash("Employee added for task successfully", "success")
    collection.insert_one({"username":username,"crime":crime})
    return redirect(url_for("admin.admin_page"))

@add_crime_blueprint.route("/add_crime", methods = ["POST"])
def Add_crime():
    crime = request.form.get("crime")
    collection = db['crime']
    exist = collection.find_one({"crime": crime})  
    print(exist)
    if exist: 
        flash("Crime already exists", "danger")
        return render_template("admin.html")
    else: 
        flash("Crime added successfully", "success")
        collection.insert_one({"crime":crime})
    return redirect(url_for("admin.admin_page"))

@add_user_blueprint.route("/addUser",methods = ["POST"])
def addUser():
    password = request.form.get("password")
    username = request.form.get("username")
    position = request.form.get("dropdown")
    collection = db['login']
    exist = collection.find_one({"username": username})
    if exist :
        flash("User already exists", "danger")
        return render_template("admin.html")
    flash("Employee added successfully", "success")
    collection.insert_one({"username":username, "password":password, "position": position})
    return redirect(url_for("admin.admin_page"))

@delete_user_blueprint.route("/deleteUser", methods = ["POST"])
def deleteUser():
    username = request.form.get("username")

    collection = db['login']
    exist = collection.find_one({"username": username})
    if not exist :
        flash("User does not exists", "danger")
        return render_template("admin.html")
    db['login'].delete_one({"username":username})
    db['user_crime'].delete_many({"username":username})
    flash("Employee removed successfully", "success")
    return redirect(url_for("admin.admin_page"))

