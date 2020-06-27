from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/test', methods=['GET'])
def test():
    return "alive"




# @app.route('/get_skeleton', methods=['GET'])
# def get_skeleton():
#     global skeleton

#     return skeleton

if __name__ == '__main__':
    app.run(host='192.168.225.50', port=5000)