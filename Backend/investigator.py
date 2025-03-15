from flask import render_template, request, Blueprint, session,  send_file
from pymongo import MongoClient
import os, datetime, pytz

client = MongoClient("mongodb+srv://ajayjoshi1908:oY3CJK3VDbJ1V0IK@decscluster.gw3pd.mongodb.net/user?retryWrites=true&w=majority")
db = client['user']

add_file_blueprint = Blueprint("file", __name__)
view_blueprint = Blueprint("view",__name__)

@add_file_blueprint.route("/addFile")
def add_file():
    username = session['username']
    collecction = db["user_crime"]
    l = [i['crime'] for i in collecction.find({'username':username})]
    print(l)
    return render_template("addFile.html", cases = l) 

@view_blueprint.route('/view', methods=['POST'])
def view_file():
    file_path = request.form.get('file_path')
    username = session['username']
    filename = request.form.get('filename')
    metadata = request.form.get('metadata')
    case = request.form.get('case')
    collection = db['history']
    ist = pytz.timezone("Asia/Kolkata") 
    local_time = datetime.datetime.now(ist).isoformat()
    collection.insert_one({
        "username": username,
        "filename": filename,
        "metadata": metadata,
        "time": local_time,
        "status": "Accessed",
        "case": case,
        "file_path": file_path
    })
    if file_path:
        try:
            return send_file(file_path, as_attachment=False)
        except Exception as e:
            return f"Server error !!\nError loading file: {str(e)}"
    return "File not found", 404

