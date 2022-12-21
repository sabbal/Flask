from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def admin():
   return 'Hello Admin!'

@app.route("/guest")
def guest():
   return 'Hello Guest!'

@app.route("/greet/<name>")
def greet(name):
    if name == 'admin':
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest"))





if __name__ == '__main__':
   app.run(port=8080)
   
