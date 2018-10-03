class Question:    
    quer_01 = '대한민국의 수도는?\n1:서울 2:도쿄 3:베이징'
    quer_02 = '미국의 수도는?\n1:서울 2:도쿄 3:워싱턴'
    
    def __init__(self, name):
        self.name = name                        
    
    @classmethod
    def show_question(cls, step):        
        if(step == 1):
            print(cls.quer_01)
        elif(step == 2):
            print(cls.quer_02)
     
    @classmethod
    def chk_answer(cls, step, answer):
        if(step == 1):
            if(answer == '1'):
                return True
            else:
                return False
        elif(step == 2):
            if(answer == '3'):
                return True
            else:
                return False
