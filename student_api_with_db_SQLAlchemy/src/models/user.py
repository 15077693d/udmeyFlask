from db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password, _id=None):
        self.username = username
        self.password = password
        self.id = _id

    def __str__(self):
        return f"<id: {self.id} username: {self.username} password: {self.password}>"

    def json(self):
        return {"username": self.username,
                "password": self.password,
                "id": self.id}

    @classmethod
    def find_all(cls):
        users = cls.query.all()
        return [user.json() for user in users]

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


if __name__ == '__main__':
    User("oscar", "123").add()
