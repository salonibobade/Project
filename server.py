from flask import Flask,render_template,request,redirect,url_for
import MySQLdb


app = Flask(__name__)
conn = MySQLdb.connect(host="localhost",user="root",password="Sallu@1811",db="testdb")

@app.route("/loggedin",methods=["POST",'GET'])
def login():
    user = request.args.get('user')
    #username = str(request.form["user"])
   # password = str(request.form["password"])
   #cursor = conn.cursor()
   # cursor.execute("SELECT * FROM user WHERE username ='"+username+"'and password='"+password+"'")
   # user = cursor.fetchone()
   # if user is None:
    #    return False 
    
    return user



if __name__ == '__main__':
    app.run(debug=True)



'''from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask import Flask,render_template,request,redirect,url_for
import MySQLdb


app = Flask(__name__)
api=Api(app)
conn = MySQLdb.connect(host="localhost",user="root",password="Sallu@1811",db="testdb")



@app.route("/loggedin",methods=["POST",'GET'])
def login():
    username = str(request.form["user"])
    password = str(request.form["password"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE Emp_ID ='"+username+"'and Emp_Password='"+password+"'")
    user = cursor.fetchone()
    if user is None:
        return False

    return True
    '''








if __name__ == '__main__':
   app.run(port=5002)