from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


from models import *


SQLALCHEMY_DATABASE_URI = 'mysql://mayank:123456@localhost:3306/project'
SQLALCHEMY_BINDS = {
    'db1': SQLALCHEMY_DATABASE_URI,
    'db2': 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="mayank",pw="12345",url="localhost:1452",db="student")
}

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/postgresql", methods=["GET"])
def get_postgresql_data():
    data = Students.query.order_by(Students.id).all()
    dataJson = []
    for i in range(len(data)):
        dataDict = {
            "id": str(data[i]).split("/")[0],
            "name": str(data[i]).split("/")[1],
            "age": str(data[i]).split("/")[2],
            "course": str(data[i]).split("/")[3],
            "phone_number": str(data[i]).split("/")[4],
        }
        dataJson.append(dataDict)
    return jsonify(dataJson)


@app.route("/mysql", methods=["GET"])
def get_mysql_data():
    data = Employee.query.order_by(Employee.id).all()
    dataJson = []
    for i in range(len(data)):
        dataDict = {
            "id": str(data[i]).split("/")[0],
            "name": str(data[i]).split("/")[1],
            "age": str(data[i]).split("/")[2]
        }
        dataJson.append(dataDict)
    return jsonify(dataJson)


if __name__ == "__main__":
    app.debug = True
    app.run()
