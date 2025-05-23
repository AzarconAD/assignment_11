from question import Question
import json

class QuizCreator:
    def __init__(self):
        self.quiz = []
    
    def add_question(self):
        question = input("Enter a question: ")
        a = input("Enter choice (a): ")
        b = input("Enter choice (b): ")
        c = input("Enter choice (c): ")
        d = input("Enter choice (d): ")
        correct_choice = input("Enter the correct choice: ")

        while True:
            if correct_choice in ["a", "b", "c", "d"]:
                new_question = Question(question, a, b, c, d, correct_choice)
                self.quiz.append(new_question)
                break
            else:
                print("Not in choices")

    def save_to_file(self, filename = "quiz.txt"):
        with open("quiz.txt", "w") as file:
            json.dump([question.dictionary() for question in self.quiz], file, indent=4)
        print(f"Quiz saved to {filename}")
    
    def run(self):
        while True:
            self.add_question()
            while True:
                another_question = input("Enter another question? (y/n) ").strip().lower()
                if another_question == "y":
                    break
                elif another_question == "n":
                    self.save_to_file()
                    return
                else:
                    print("Please enter y or n")
                    