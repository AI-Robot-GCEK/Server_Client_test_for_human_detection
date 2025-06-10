from flask import Flask, jsonify, request

app = Flask(__name__)

human_value = 0


@app.route("/human", methods=["GET", "POST"])
def human():
    global human_value
    if request.method == "GET":
        return jsonify({"human_value": human_value}), 200
    elif request.method == "POST":
        data = request.get_json() or {}
        human_value = data["human_value"]
        print(human_value)
        return (
            jsonify({"message": "POST request received at /human", "data": data}),
            200,
        )


if __name__ == "__main__":
    app.run(debug=True)
    human_value = 1
