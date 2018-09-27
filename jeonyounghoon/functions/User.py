class User:
    user_list= []

    def __init__(self,name):
        self.name=name
        self.life=10
        self.score=0
        self.user_list.append(self)
        
    def __repr__(self):
          return f'repr {self.name},{self.life},{self.score}'
    
    def __str__(self):
        print (f'str{self.name},{self.life},{self.score}')
    
