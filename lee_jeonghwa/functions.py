import time
import random

class Users:
    def __init__(self, name, score = -1):
        self.name = name
        self.score = score

    def __repr__(self):
        return repr((self.name, self.score))

    def add_result_to_file(self):
        with open('score.txt', 'at') as f:
            f.write(f'{self.name}, {self.score}\n')

########################################################################

class Ranking:
    '''
    처음에 랭킹을 보여주는데 필요한  class
    랭킹은 같은 이름이 어려번 나올 수 있다.
    '''
    def ranking(self):
        users = []
        with open('score.txt', 'rt') as f:
            while True:
                line = f.readline()
                if line:
                    line = line.split(',')
                    users.append(Users(line[0], float(line[1])))
                else:
                    break
        if users:
            return sorted(users,  key = lambda user: user.score)
        else:
            return users

    def show_ranking(self):
        users = self.ranking()
        if users:
            for index, r in enumerate(users, start = 1):
                print(f'{index}위  {r.name}:\t {r.score}초')
                if index == 5:
                    break
        else:
            print('아직 등록된 사용자가 없습니다')

#####################################################
class MultiplicationGame:

    '''
    게임을 진행하는데 필요한 모든 method를 포함한다
    '''
    def __init__(self, user):
        self.user = user #user는 User class에서 만들어진 인스턴스이다

    def one_problem(self):
        a = random.randint(2,12)
        b = random.randint(2,12)
        result = input(f'{a} X {b} = ')
        if int(result) == a*b:
            return True
        else:
            return False

    def problem_sets(self):
        panalty = 0
        for i in range(10):
            if self.one_problem():
                print('정답입니다 *^^*')
            else:
                panalty +=1
                print(f'오답입니다. {panalty}회 틀림')
            if panalty == 3: #3번 틀리면
                print('3회 오류로 실패 !!!!!!!!')
                break
        return panalty

    def calculate_score(self):
        start = time.time()
        panalty = self.problem_sets()
        end = time.time()

        if panalty == 3: #실패
            return -1
        else:
            return round(end-start + 3*panalty,  3) # 소수점아래 3자리까지 표현

    def repeat_game(self):
        while True:
            score = self.calculate_score()
            if score == -1:
                print('게임에 실패하여 결과를 저장하지 않습니다')
            else:
                print(f'{self.user.name}님의 결과는 {score}초 입니다')
                if score < self.user.score or self.user.score == -1 :
                    self.user.score = score
                    print('최고 기록이 갱신 되었습니다!!! ')
            continue_char = input('\n계속 하시겠습니까? [y/]')
            if continue_char == 'y':
                pass
            else:
                print(f'{self.user.name}님의 결과는 {self.user.score}초로 기록됩니다')
                self.user.add_result_to_file()
                break
