class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score if 0 <= score <= 10 else 0
