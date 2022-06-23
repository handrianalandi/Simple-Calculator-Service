import time
from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_mysqldb import MySQL
from datetime import timedelta
from uuid import uuid4
from calculation import prime_index,palindrome_prime_index
app = Flask(__name__)

#run celery with
# celery -A calculation  worker -l info -P eventlet

# session.clear()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'simplecloud'
mysql = MySQL(app)

#flask session secret key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

def set_session_timeout(minute):
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=minute)

@app.route("/")
def home():
    # set_session_timeout(minute=1)
    return "Hello, Flask!!asdsd"

@app.route("/testing",methods=['POST'])
def testing():
    #get request body with key "name" json
    name = request.json['name']
    print(name)
    return name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if session.get('logged_in'):
        return f"You are already logged in as {session['username']}!"
    if request.method == 'GET':
        return "Wrong method!"
    if request.method == 'POST':
        #get username form request body
        username = request.json['username']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            #set secret key for session
            session['secret_key'] = str(uuid4())
            session['username'] = username
            session['logged_in'] = True
            set_session_timeout(minute=1)
            return f"Welcome {username}"
        else:
            return "Invalid username or password"

#logout
@app.route('/logout', methods = ['POST'])
def logout():
    print("test")
    if(session.get('username')):
        session.clear()
        return "Logged out"
    return "You are not logged in"

#register
@app.route('/register', methods = ['POST'])
def register():
    if (session.get('username')):
        return f"You are already logged in as {session['username']}!"
    if request.method == 'POST':
        #get username form request body
        username = request.json['username']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        #register user to db
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cursor.close()
        return "Registered, please login before using the app"

@app.route('/api/prime/<n>', methods = ['GET'])
def prime(n):
    print("test")
    if not session.get('logged_in'):
        return "You are not logged in"
    if request.method == 'GET':
        prime_index.delay(n)
        #return jsonify result of prime_index function
        return "Prime Task has been called please see your celery terminal to see the result"

# palindrome
@app.route('/api/prime/palindrome/<n>', methods = ['GET'])
def palindromeprimeindex(n):
    if not session.get('logged_in'):
        return "You are not logged in"
    if request.method == 'GET':
        palindrome_prime_index.delay(n)
        # return jsonify({"result": palindrome_prime_index(n)})
        return "Palindrom Prime Task has been called please see your celery terminal to see the result"

if(__name__ == "__main__"):
    app.run(debug=True)