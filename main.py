from flask import *
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/adminpannel",methods=['POST','GET'])
def adminpannel():
    if request.method == 'POST':
        email = request.form['em']
        password = request.form['pswd']
        if email == "admin@gmail.com" and password == "admin123":
            subprocess.call(["python","bill.py"])
    return redirect(url_for("home")) 


        

if __name__ == '__main__':
    app.run(debug=True)

    