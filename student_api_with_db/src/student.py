class Student:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return f"<name: {self.name} sex: {self.sex} age: {self.age}>"

