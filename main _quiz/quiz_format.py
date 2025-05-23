import random
from file_reading import FileReading

class QuizFormat:
    def format(self, score):
        reader = FileReading()
        quiz = reader.quiz
        score = 0
        total = len(quiz)

        random.shuffle(quiz)
        
        for questions in quiz:

            print("Question:", questions["question"])
            print("a.)", questions["a"])
            print("b.)", questions["b"])
            print("c.)", questions["c"])
            print("d.)", questions["d"])

            # ask user for their answer
            user_answer = input("Answer: ").lower().strip()

            # display the correct answer
            key = questions["correct_choice"]
            correct_answer = questions[key]
            print("Correct answer:", key)

            # if answer is correct add 1 else no score
            if user_answer == key:
                score += 1

        # display final score
        print(f"Your final score is {score}/{total}")