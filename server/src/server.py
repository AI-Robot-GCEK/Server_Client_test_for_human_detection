from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial human presence state
human_state = {"value": 0}

@app.route('/human', methods=['GET'])
def get_human_state():
    return jsonify(human_state)

@app.route('/update', methods=['POST'])
def update_human_state():
    data = request.json
    if 'value' in data and data['value'] in [0, 1]:
        human_state['value'] = data['value']
        return jsonify({"message": "State updated", "value": human_state['value']})
    else:
        return jsonify({"error": "Invalid value"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
