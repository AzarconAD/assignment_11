from question import Question

class QuizCreator:
    def __init__(self):
        self.quiz = []
    
    def AddQuestion(self):
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