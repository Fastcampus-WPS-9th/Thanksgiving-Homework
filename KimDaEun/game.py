from functions.user import User
from functions.card import Card
from functions.computer import Computer
from functions.deck import Deck
from collections import OrderedDict

if __name__ == '__main__':
    print('---------- 원카드 게임 -----------')

    user_ranks = {}
    with open('./save_data/record.txt', 'rt') as record:
        for line in record.readlines():
            user_record = line.split(' ')
            user_name = user_record[0]
            user_score = int(user_record[1].split('\n')[0])
            user_ranks[user_name] = user_score
    user_ranks = OrderedDict(sorted(user_ranks.items(), key=lambda t: t[1], reverse=True))

    print('유저 랭킹')
    for key, value in user_ranks.items():
        print(key, ': ', value)

    user = User(input('이름을 입력하세요 : '))
    computer = Computer('computer')
    winner, loser = None, None

    Deck.initiate(user, computer)
    print('\n------ 게임을 시작합니다. ------\n')

    try:
        while True:

            top_of_file = Deck.get_top_of_pile()
            print(f'\n현재 올라온 카드 : {Card.SHAPE[top_of_file.suit]}{top_of_file.rank}\n')

            user.show()
            user.play()
            if user.get_status() is not None:
                winner = user
                loser = computer
                break

            top_of_pile = Deck.get_top_of_pile()
            if top_of_pile.rank == '7' and isinstance(top_of_pile.drawer, User):
                print('7을 내면 카드의 모양을 바꿀 수 있습니다.')
                user.change_suit()

            computer.play()
            computer.show()
            if computer.get_status() is not None:
                winner = computer
                loser = user
                break

            top_of_pile = Deck.get_top_of_pile()
            if Deck.get_top_of_pile().rank == '7' and isinstance(top_of_pile.drawer, Computer):
                computer.change_suit()

        print(f'{winner.name}님이 우승하였습니다.')

        winner.score += 50
        loser.score -= 50

        print(f'{winner.name}님의 현재점수 : {winner.score}')
        print(f'{loser.name}님의 현재점수 : {loser.score}')

        with open('./save_data/record.txt', 'rt') as file:
            updated_records = []
            user_record = ' '.join([user.name, str(user.score)])
            computer_record = ' '.join([computer.name, str(computer.score)])

            for line in file.readlines():
                signed_player_name = line.split(' ')[0]
                if signed_player_name == user.name:
                    updated_records.append(user_record)
                elif signed_player_name == computer.name:
                    updated_records.append(computer_record)
                else:
                    updated_records.append(line)

        if user_record not in updated_records:
            print("user", user_record)
            updated_records.append(user_record)

        with open('./save_data/record.txt', 'wt') as file:
                file.write('\n'.join(updated_records))

    except ValueError as value_err:
        print(value_err)
