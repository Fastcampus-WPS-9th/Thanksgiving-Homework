import sys
import random
import time

class User:
    user_list = list()
    
    def __init__(self, name):
        self.name = name
        self.__best_score = 0
        self.__best_time = 0
        self.user_list.append(self)
        print("=" * 30)
        print(f'User Name: [{self.name}] is created')
        print("=" * 30)
        
    def __repr__(self):
        return f'User Name: {self.name}(ID Number: {id(self)})'
    
    @property
    def best_score(self):
        return self.__best_score
    
    @best_score.setter
    def best_score(self, score):
        self.__best_score = score
    
    @property
    def user_cnt(self):
        return len(self.user_list)
    
    @classmethod
    def get_score_ranking(cls):
        if cls.user_list == []:
            print("There is no user")
        else:
            user_list = [user.name for user in cls.user_list]
            score_list = [user.best_score for user in cls.user_list]
            user_score = zip(user_list, score_list)
            ranking_score = sorted(user_score, key= lambda x: x[1], reverse= True)
            ranking_result = ""
            for idx, ranking in enumerate(ranking_score, 1):
                ranking_result += f'{idx}. User Name: {ranking[0]}, Score: {ranking[1]}\n'
            return ranking_result
        
    @property
    def info(self):
        print(f'User Name: {self.name}\nBest Scoore: {self.best_score}\nBest Time: {self.best_time}')


class Question:
    q_list = list()
    
    def __init__(self, content):
        if content in [q.content for q in self.q_list]:
            print("이미 존재하는 문항입니다.")
            self.content = content
        else:
            self.content = content 
            self.q_list.append(self)
            print(f'Q.[{self.content}] is added')
        
    def __repr__(self):
        return f'Q: {self.content}(ID: {id(self)})'
    
    @property
    def q_cnt(self):
        return len(self.q_list)


class Play:
    def __init__(self):
        while True:
            print("""
            
            === Typing in 1 second! ===
            1. Start Game
            2. Ranking
            0. Exit
            ===========================
            
            """)
            menu = input("Press the number: ")
            if menu == str(0):
                print("Exit Game")
                break
            
            elif menu == str(2):
                try:
                    with open('ranking.txt', 'r') as f:
                        contents = f.read()
                        print(f'{"=" * 20} Score Ranking {"=" * 20}\n')
                        print(contents)
                        print("=" * 55)
                except FileNotFoundError:
                        print("현재 랭킹기록이 존재하지 않습니다.")
                        continue
                        
            
            elif menu == str(1):    
                id_crt = False
                while isinstance(id_crt, User) != True:
                    new_id = input("Enter your user name: ")
                    if new_id in [user.name for user in User.user_list]:
                        for user in User.user_list:
                            if new_id == user.name:
                                record_q = input("이전 플레이 기록이 있습니다. 이 계정을 사용려면 [y], 새로 계정을 만드려면 아무키나 눌러주세요: ")
                                if record_q == 'y':
                                    id_crt = user
                                    print("현재 계정은 [{}]입니다.".format(user.name))
                                    break
                                else:
                                    break
                    else:
                        id_crt = User(new_id)

                while True:
                    self.play(id_crt)
                    try_again = input("다시하기는 [y], 그만하시려면 아무키나 눌러주세요: ")
                    if try_again == "y":
                        pass
                    else:
                        break

            else:
                print("""
                
                *** Press only number on the menu ***
                
                """)
                continue
        
    def play(self, id_crt):
        life = 3
        crt_score = 0
        print("""
        
        ########## Start Game! ##########
        
        """)
        while life > 0:
            answer = random.choice([q.content for q in Question.q_list])
            print(">>>", answer)
            start_time = time.time()
            your_answer = input("--> ")
            end_time = time.time()
            duration = end_time - start_time
            if duration > 1:
                life -= 1
                print("""
                ------------------------
                  ** ⌛️ Time Over! **
                
                               Life {}{}
                ------------------------
                """.format("♥︎"*life,"♡"*(3-life)))
            elif answer != your_answer:
                life -= 1
                print("""
                -------------------------
                 ** 😂 Wrong Answer! **
                
                               Life {}{}
                -------------------------
                """.format("♥︎"*life,"♡"*(3-life)))
            else:
                crt_score += 1
                print("                            ** Score: {} **".format(crt_score))
        
        print("""
          === Game Over ===
          Your Score: {}
          =================
        """.format(crt_score))
        if crt_score > id_crt.best_score:
            id_crt.best_score = crt_score
        with open('ranking.txt', 'w') as f:
            f.write(User.get_score_ranking())

if __name__ == "__main__":
    Question('a')
    Question('b')
    Question('c')
    Question('d')
    Question('e')
    Question('f')
    Question('g')
    Question('h')
    Question('i')
    Question('j')
    Question('k')
    Question('l')
    Question('m')
    Question('n')
    Question('o')
    Question('p')
    Question('q')
    Question('r')
    Question('s')
    Question('t')
    Question('u')
    Question('v')
    Question('w')
    Question('x')
    Question('y')
    Question('z')
    Question('AA')
    Question('BB')
    Question('CC')
    Question('GG')
    Question("*")
    
    Play()