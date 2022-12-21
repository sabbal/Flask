from flask import Flask,request
app = Flask(__name__)

@app.route("/json", methods=['POST'])
def login():
    body = request.get_json()
    user_name = body['user_name']
    channel = body['channel']
    message = 'Dear '+ user_name +', you have been subscribed to "'+channel+'" !'
    return message




if __name__ == '__main__':
   app.run(port=8080)
   
