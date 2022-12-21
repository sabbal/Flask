from flask import Flask,request

app = Flask(__name__)

@app.route("/bio", methods=['POST'])
def upload_bio():
    f = request.files['bio']
    f.save(dst="c:/flask_uploads/bio.txt")
    return 'uploaded successfully'




if __name__ == '__main__':
   app.run(port=8080)
   
