from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources = {r"/*": { "origins": "*"}})

@app.route('/home/',methods=['GET'])
def home():
    datainfo = """
    Python Flask Server Connection Success....
    """
    return jsonify(datainfo)

@app.route('/data',methods=['GET'])
def data():
    data = "signal not found yet"
    return jsonify(data)


@app.route('/about', methods=['GET'])
def about():
    productInfo = """
    Thanks for use our product built in pyhton Flask and Vue js, please contact with us in facebook
    """
    return jsonify(productInfo)
