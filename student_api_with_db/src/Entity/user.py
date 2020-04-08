class User:
    # id is python keyword
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def __str__(self):
        return f"<id: {self.id} username: {self.username} password: {self.password}>"

