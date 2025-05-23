from file_reading import FileReading
from quiz_format import QuizFormat

if __name__=="__main__":
    reader = FileReading()            
    quiz_data = reader.quiz             
    quiz = QuizFormat(quiz_data)        
    quiz.format() 