from flask import Flask,render_template,request,redirect,url_for
import MySQLdb
from flask_cors import CORS,cross_origin
import flask


app = Flask(__name__)
CORS(app)
conn = MySQLdb.connect(host="localhost",user="root",password="Sallu@1811",db="testdb")

@app.route("/loggedin",methods=["POST",'GET'])
def login():

    username = request.args.get('user')
    password=request.args.get('password')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username ='"+username+"'and password='"+password+"'")
    user = cursor.fetchone()

    if user is None:
        response = flask.jsonify({"status":"false"})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        return response
    response = flask.jsonify({"status":"true"})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    
    return response
    #return user



if __name__ == '__main__':
    app.run(debug=True)


