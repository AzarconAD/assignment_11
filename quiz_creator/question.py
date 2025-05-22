class Question:
    def __init__(self, question, a, b, c, d, correct_choice):
        self.question = question
        self.choices = {
            "a" : a,
            "b" : b,
            "c" : c,
            "d" : d
        }
        self.correct_choice = correct_choice
    def dictionary(self):
        return {
            "question": self.question,
            "a": self.choices["a"],
            "b": self.choices["b"],
            "c": self.choices["c"],
            "d": self.choices["d"],
            "correct_choice": self.correct_choice
        }