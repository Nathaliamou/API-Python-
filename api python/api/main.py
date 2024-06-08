from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/users/<user_id>")
def get_user(user_id): 
    user = {"id": user_id, "name": "test", "telefono": "3147277149"}
    # /users/2654?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()  # Obtiene los datos JSON del cuerpo de la solicitud
    data['status'] = "user created"
    return jsonify(data), 201  # Devuelve los datos en formato JSON con el código de estado 201 (Created)

if __name__ == "__main__":
    app.run(debug=True)
