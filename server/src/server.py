from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/human", methods=["GET", "POST"])
def human():
    if request.method == "GET":

        return jsonify({"human_value": 1}), 200
    elif request.method == "POST":
        data = request.get_json() or {}
        return (
            jsonify({"message": "POST request received at /human", "data": data}),
            200,
        )


if __name__ == "__main__":
    app.run(host="172.16.32.104", debug=True)
