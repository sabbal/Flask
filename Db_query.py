from flask import Flask,request
import mysql.connector
app = Flask(__name__)
dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="college"
)

@app.route("/db", methods=['POST'])
def login():
    body = request.get_json()
    name = body['name']
    cursorObject = dataBase.cursor()

    query = "SELECT distinct(NAME), Roll_no FROM college.STUDENT where NAME = %s"
    cursorObject.execute(query, (name,))

    myresult = cursorObject.fetchall()
    message = ''
    for x in myresult:
        message += str(x)

    # disconnecting from server
    dataBase.close()


    return message




if __name__ == '__main__':
   app.run(port=8080)
   
