from functions.question import *
from functions.answer import *
from functions.user import *

def turn_on():
    print('= Turn on game =')
    score = 0;
    while True:
        choice = input(
            'What would you like to do?\n'
            ' 1: Play Game\n'
            ' 0: Exit\n'
            'Input: '
        )
        
        if choice == '1':            
            question = Question('게임시작')            
            user_name = input(
                'user_name: '
            )
            user = User(user_name,0)
            for step in range(1,3):                                                                                
                question.show_question(step)
                answer = input(
                    'Answer: '
                )
                chk_answer = Answer(step,answer)                                
                if(chk_answer.return_answer(question)):
                    print('정답입니다')
                    score += step    
                else:
                    print('틀렸습니다')
                
            user.input_score(score)
            temp = user.return_score()
            with open('score_rank.txt','at') as f:
                f.write(temp)
                f.close()
            break
        elif choice == '0':
            break
        else:
            print('Choice not exist')
        print('--------------------------')
    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()
