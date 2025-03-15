from flask import render_template, request, Blueprint,send_from_directory, session
from pymongo import MongoClient
import os, datetime, pytz
from Backend.helper import get_investigator_cases, get_file_info

client = MongoClient("mongodb+srv://ajayjoshi1908:oY3CJK3VDbJ1V0IK@decscluster.gw3pd.mongodb.net/user?retryWrites=true&w=majority")
db = client['user']

UPLOAD_FOLDER = "uploads"  
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


upload_file_blueprint = Blueprint('upload', __name__)
view_blueprint = Blueprint("view", __name__)

@upload_file_blueprint.route("/upload_file", methods=['POST'])
def upload():
    file = request.files.get('file')
    file_name = request.form.get('file_name') 
    metadata = request.form.get('metadata')
    selected_item = request.form.get("cases")
    username = session.get('username') 
    collection = db['history']

    exist = collection.find_one({"filename": file_name, "case": selected_item})
    if exist:
        cases = get_investigator_cases(session['username'])
        file_info = get_file_info(username)
        return render_template("investigator.html", cases=cases, grouped_files=file_info)

    case_folder = os.path.join(UPLOAD_FOLDER, selected_item)
    os.makedirs(case_folder, exist_ok=True) 

    file_extension = os.path.splitext(file.filename)[1]
    safe_file_name = f"{file_name}{file_extension}"
    file_path = os.path.join(case_folder, safe_file_name)
    file.save(file_path)
    ist = pytz.timezone("Asia/Kolkata") 
    local_time = datetime.datetime.now(ist).isoformat()
    collection.insert_one({
        "username": username,
        "filename": file_name,
        "metadata": metadata,
        "time": local_time,
        "status": "Uploaded",
        "case": selected_item,
        "file_path": file_path
    })
    collection = db['uploads']
    collection.insert_one({
        "username": username,
        "filename": file_name,
        "metadata": metadata,
        "time": local_time,
        "status": "Uploaded",
        "case": selected_item,
        "file_path": file_path
    })

    cases = get_investigator_cases(session['username'])
    file_info = get_file_info(username)
    print("upload function", file_info)

    return render_template("investigator.html", cases=cases, grouped_files=file_info)


