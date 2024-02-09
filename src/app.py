from flask import Flask
from flask import Response
app = Flask(__name__)
@app.get("/users/<id>")
def get_user(id:int):
    return Response()