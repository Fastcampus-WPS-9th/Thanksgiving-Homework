import time
import signal
from .Players import *


class InGame:

    ONE_VALUE = 1

    def __init__(self):
        self.__total_played_time = 0

    @staticmethod
    def input_user_id_and_name():
        print("[!] Please enter your id and name.")
        print("[!] ID: ")
        user_id = input()
        print("[!] Name: ")
        user_name = input()

        id_name_data = Players(user_id=user_id, user_name=user_name)

        return id_name_data

    @staticmethod
    def when_the_question_is_given(questions):
        '''
        TODO: 시간제한을 걸고 맞추면 플러스점수, 틀리면 마이너스 점수.
        문제를 받는다.
        시간을 잰다.
        제한시간 이내에 못하면 -1리턴
        풀면 유저ID, 이름, 점수, 남은생명 리턴.
        :return:
            when player failed the quiz, it returns -1
            when player solves all the quiz, it returns list
            about userID, name, score, player_life
        '''

        id_name_data = InGame.input_user_id_and_name()

        start_time = time.time()
        for current_question in questions:

            print(current_question[0])
            answer = input()
            if answer != str(current_question[1]):
                id_name_data.current_life = InGame.ONE_VALUE
                print("[x] wrong answer....")
            if id_name_data.current_life == 0:
                print("-----------------------")
                print("|    [x] GAME OVER    |")
                print("-----------------------")
                print("[!] please try again..|")
                print("-----------------------")
                return -1

        print("[O] WELL DONE!!")
        achieved_score = round(time.time() - start_time, 3) + id_name_data.current_score

        clearer = [
            id_name_data.user_id,
            id_name_data.user_name,
            id_name_data.current_life,
            achieved_score,
            InGame.ONE_VALUE,
        ]
        # 총 플레이타임
        print("수행 시간: ", round(time.time() - start_time, 3))

        return clearer