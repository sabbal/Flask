from flask import Flask
app = Flask(__name__)

@app.route("/asdf")
def asdf():
   return 'asdfkjasdfgaskjvbas asdfasdfhdhsadgkf'

@app.route("/greet/<name>")
def greet(name):
    greet_message = 'Hello '+name+" !"
    return greet_message




if __name__ == '__main__':
   app.run(port=8080)
   
