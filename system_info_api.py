from flask import Flask, jsonify, request 
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Store CPU and RAM data globally
resource_data = {"cpuLoad": 0, "ramUsage": 0, "totalRam": 0}

@app.route('/resources', methods=['GET'])
def get_resources():
    return jsonify(resource_data)

@app.route('/update_resources', methods=['POST'])
def update_resources():
    global resource_data
    resource_data = request.get_json()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
