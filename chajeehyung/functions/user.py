class User:
    def __init__(self, user_name, score):
        self.user_name = user_name
        self.score = score        
        
    def input_score(self,score):        
        self.score = score
        
    def return_score(self):        
        return self.user_name +':'+ str(self.score)+' '
