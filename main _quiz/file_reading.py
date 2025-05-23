import json

class FileReading:
    def __init__(self):
        with open("quiz.txt", "r") as file:
            quiz = json.loads(file)
        self.quiz = quiz