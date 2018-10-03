class Answer:
    def __init__(self, step, answer):        
        self.step = step
        self.answer = answer
        
    def return_answer(self, question):
        return question.chk_answer(self.step, self.answer)
