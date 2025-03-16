from pymongo import MongoClient
from collections import defaultdict
import os, datetime
client = MongoClient("mongodb+srv://ajayjoshi1908:oY3CJK3VDbJ1V0IK@decscluster.gw3pd.mongodb.net/user?retryWrites=true&w=majority")
db = client['user']

UPLOAD_FOLDER = os.path.abspath("uploads") 


def get_investigator_cases(username):
    collection = db['user_crime']
    cases = [i['crime'] for i in collection.find({"username": username})]
    print(cases)
    return cases

def get_file_info(username):
    collection = db['uploads']
    files = collection.find({"username": username})

    grouped_files = defaultdict(list)
    for file in files:
        case_name = file.get("case", "Uncategorized")  
        grouped_files[case_name].append(file)
    
    return grouped_files
def get_file_info2(username):
    collection = db['user_crime']
    
    crimes = collection.find({"username": username})
    user_crimes = [crime["crime"] for crime in crimes] 

    collection = db['uploads']

    files = collection.find({"case": {"$in": user_crimes}})

    grouped_files = defaultdict(list)
    for file in files:
        case_name = file.get("case", "Uncategorized")  
        grouped_files[case_name].append(file)
    
    return grouped_files

def all_files():
    collection = db['uploads']
    files = collection.find({})
    grouped_files = defaultdict(list)
    for file in files:
        case_name = file.get("case", "Uncategorized")  
        grouped_files[case_name].append(file)
    return grouped_files

def get_history():
    collection = db['history']
    files = collection.find({})
    return files

def get_all_users():
    collection = db['login']
    l = [[i['username'],i['position'] ]for i in collection.find({})]
    return l

def emp_case():
    collection = db['user_crime']
    emp_crime_dict = {}

    for record in collection.find({}):
        username = record['username']
        crime = record['crime']
        
        if username in emp_crime_dict:
            emp_crime_dict[username].append(crime)  
        else:
            emp_crime_dict[username] = [crime] 

    return emp_crime_dict 