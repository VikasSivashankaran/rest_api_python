from flask import json


class User:
    id = 0
    email = ''
    password = ''
    user_name = ''
    course=''

    def __init__(self, id, email, password, user_name,course ):
        self.id = id
        self.email = email
        self.password = password
        self.user_name = user_name
        self.course=course

    def __str__(self) -> str:
        return f"{self.id} - {self.email}  - {self.password} - {self.user_name} - {self.course})"

    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)
