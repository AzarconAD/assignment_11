import json

class FileReading:
    def __init__(self):
        with open("quiz.txt", "r") as file:
            self.quiz = json.loads(file)