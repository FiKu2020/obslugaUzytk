from flask import Flask , Response ,jsonify

app = Flask(__name__)

temp = []

@app.route('/users',methods=['GET'])
def get_users():
    pass

@app.get("/users/<id>",methods=['GET'])
def get_user(id:int):
    return Response()

@app.route('/users',methods=['POST'])
def create_user():
    pass    