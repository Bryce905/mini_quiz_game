# author: Bryce Henderson

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer



class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []
            
    def addQuestion(self, q):
        self.questions.append(q)

    def runQuestion(self):
            q = self.questions[0]
            print(q.text)
            for choice in q.choices:
                 print(choice)
            guess = input()
            if (guess == q.answer):
                 print("Correct!")
            else: print("Wrong!")




myQuiz = Quiz("Capitals")
q1text = "What is the Capital of Oklahoma?"
q1choices = ["Austin", "Oklahoma City", "Little Rock", "Tulsa"]
q1answer = "Oklahoma City"

q1 = Question(q1text, q1choices, q1answer)
myQuiz.addQuestion(q1)
myQuiz.runQuestion()