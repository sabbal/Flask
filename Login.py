from flask import Flask,request
app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'sabbal' and password == 'mota' :
        message = 'you are a valid user !'
    else:
        message = 'get lost!!!'
    return message




if __name__ == '__main__':
   app.run(port=8080)
   
