import random

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    
    
def playGame():
    
    num_list = random.sample(range(1, 10), 3)
    strike = 0
    ball = 0
    count = 0
    name = input("이름을 입력하세요 : ")
    
    print("숫자 야구 게임")
    print("20번 안에 정답을 맞추세요")
    while (strike < 3):
        strike = 0
        ball = 0
        my_num1 = int(input("First num : "))
        my_num2 = int(input("Second num : "))
        my_num3 = int(input("Third num : "))
        
        my_list = [my_num1,my_num2,my_num3]
        
#         print(num_list)
        for i in range(0, 3):
            for j in range(0, 3):
                if(num_list[i] == my_list[j] and i == j):
                    strike += 1
                elif(num_list[i] == my_list[j] and i != j):
                    ball += 1
        print("―――――――――――――――――――――――――――――――――――――――――――――――――")
        print(f'Result :  Strike : {strike} Ball : {ball}')
        print("―――――――――――――――――――――――――――――――――――――――――――――――――")
        count += 1
        if count > 19:
            print("Game Over")
            break
    if count < 20:
        print(f'The number of times you tried : {count}')
        p1 = Player(name, count)
        f = open('ranking.txt', 'at')
        f.write(f'이름 : {p1.name} 시도횟수 : {p1.score}\n')
        f.close
        
def checkRank():
    f = open('ranking.txt', 'rt')
    lines = f.readlines()
    f.close()
    print("―――――――――――――――――――――――――――――――――――――――――――――――――")
    print(f'                    Ranking                     ')
    print("―――――――――――――――――――――――――――――――――――――――――――――――――")
    for line in lines:
        print(line)
        
        
def runGame():
    f = open('ranking.txt', 'at')
    f.close
    while True:
        choice = input('= Number Baseball =\n'
	'  1: Play Game\n'
	'  2: Check Ranking\n'
	'  0: Exit\n'
	'    Input : ')
        if choice == '0':
            break
        elif choice == '1':
            playGame()
        elif choice == '2':
            checkRank()
        else:
            print('Choice not exist')
        print("―――――――――――――――――――――――――――――――――――――――――――――――――")

    print('= Turn off game =')

if __name__ == '__main__':
    runGame()
