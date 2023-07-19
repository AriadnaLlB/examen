from flask import Flask, jsonify
from repository import Usuarios

app = Flask(__name__)

# Inicializamos el repositorio de usuarios
repository = Usuarios()

@app.route('/create/user/<int:user_id>/<string:user_name>/<int:user_age>', methods=['POST'])
def create_user(user_id, user_name, user_age):
    repository.add(user_id, user_name, user_age)
    return jsonify("usuario creado")

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = repository.get(user_id)
    if user:
        return jsonify(user)
    return jsonify("usuario no encontrado"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)