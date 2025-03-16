from flask import render_template, request, Blueprint, session
from pymongo import MongoClient
from Backend.helper import get_investigator_cases, get_file_info, all_files, get_history, get_file_info2, get_all_users, emp_case
client = MongoClient("mongodb+srv://ajayjoshi1908:oY3CJK3VDbJ1V0IK@decscluster.gw3pd.mongodb.net/user?retryWrites=true&w=majority")
db = client['user']

login_blueprint = Blueprint("login", __name__)
admin_blueprint = Blueprint("admin", __name__)
investigator_blueprint = Blueprint('investigator', __name__)

@login_blueprint.route("/check_login", methods = ["POST"])
def Login():
    selected_item = request.form.get('dropdown')
    name = request.form.get("username")
    passw = request.form.get("password")
    session['username'] = name
    collection = db["login"]
    exist = collection.find({"username" : name, "password" : passw, "position":selected_item})
    if exist: 
        if selected_item=='Admin':
            collection = db["crime"]
            crimes = [doc["crime"] for doc in collection.find({})] 
            grouped_files = all_files()
            history = get_history()
            users = get_all_users()
            employee_crime = emp_case()
            return render_template("admin.html", crimes=crimes, grouped_files=grouped_files, history_data=history, employees = users, employee_crime=employee_crime)
        elif selected_item=='Investigator':
            cases = get_investigator_cases(name)
            file_info = get_file_info(name)
            return render_template("investigator.html", cases = cases, grouped_files=file_info)
        elif selected_item=='Analyst':
            cases = get_investigator_cases(name)
            file_info = get_file_info2(name)
            print(file_info)
            return render_template("analyst.html", cases = cases, grouped_files=file_info)

    return render_template('login', "User doesn't exist")

@admin_blueprint.route("/admin")
def admin_page():
    crimes = [doc["crime"] for doc in db['crime'].find({})]
    grouped_files = all_files()
    history = get_history()
    users = get_all_users()
    employee_crime = emp_case()
    return render_template("admin.html", crimes=crimes, grouped_files=grouped_files, history_data=history, employees = users, employee_crime=employee_crime)

@investigator_blueprint.route('/investigatorPage', methods=['POST', 'GET'])
def investigator_Page():
    name = session['username'] 
    cases = get_investigator_cases(name)
    file_info = get_file_info(name)
    return render_template("investigator.html", cases = cases, grouped_files=file_info)