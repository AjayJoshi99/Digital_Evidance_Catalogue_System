from flask import Flask, render_template
from  Backend.login import login_blueprint
from  Backend.login import admin_blueprint
from  Backend.login import investigator_blueprint
from  Backend.logout import logout_blueprint
from Backend.admin import add_crime_blueprint
from Backend.admin import add_user_crime_blueprint
from Backend.admin import add_user_blueprint
from Backend.admin import delete_user_blueprint
from Backend.investigator import add_file_blueprint
from Backend.investigator import view_blueprint
from Backend.upload import upload_file_blueprint

app = Flask(__name__, static_folder='static')  
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(add_crime_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(add_user_crime_blueprint)
app.register_blueprint(add_user_blueprint)
app.register_blueprint(delete_user_blueprint)
app.register_blueprint(add_file_blueprint)
app.register_blueprint(upload_file_blueprint)
app.register_blueprint(view_blueprint)
app.register_blueprint(investigator_blueprint)

app.secret_key = '123@Ajay' #for session
@app.route("/")
def Login():
    return render_template("login.html", error = "")




if __name__ == "__main__":
    app.run(debug=True)  
 
