from flask import Flask, = jsonify =
from data = data

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({"data: data,"message":"success"}), 200
if _name__ == "_main__":
    app.run()

