import functions, random
from functions.penalty_kick import User, Game, Leaderboard

def turn_on():
    print('== Welcome to the arcade ==')
    user = User(input('Please enter your name : '))
    score = Leaderboard(user.name, user.game.points)
    score.read_score()
    while True:
        try:
            select = int(input(f'''
            Hello {user.name}!
            what would you like to do?\n
             1: earn coins \n
             2: play game\n
             0:exit \n
             Input : '''))
            if select == 1:
                number = int(input('''
                1. 3 lives guaranteed
                2. gamble(0 to 10)
                0. exit
                input :
                '''))
                try:
                    if number == 1:
                        user.earn_coins(3)
                        print('you earned 3 lives!')
                    elif number == 2:
                        number = random.randrange(0,11)
                        user.earn_coins(number)
                        print(f'you earned {number} lives!')
                    elif number == 0:
                        print('back to main...')
                        break
                except ValueError:
                    print('must select from 1,2 or 0')

            elif select == 2:
                print("Good idea! let's play a game")
                user.game.how_to()
                user.play()
                score.add_score()
            elif select == 0:
                print('Come again!')
                print('exiting game...')
                break
        except ValueError:
            print('must choose from 1, 2, or 0')

turn_on()
