import json

class FileReading:
    def __init__(self, filename = "quiz.txt"):
        with open(filename, "r") as file:
            self.quiz = json.load(file)