class Usuarios:
    def __init__(self):
        self.users = {}

    def add(self, id, name, age):
        user = {
            'id': id,
            'name': name,
            'age': age
        }
        self.users[id] = user

    def get(self, user_id):
        return self.users.get(user_id)