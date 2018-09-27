# -*- coding:utf-8 -*-

import os
import sys
from .Queries import *
from .InGame import *


class Menu:
    db_file = os.path.join(os.getcwd(), 'data/chuseok_jeopardy.db')

    def __init__(self):
        self.questions = {}

    @staticmethod
    def print_menu():
        print("----------------")
        print("[Jeopardy] 1:100")
        print("----------------")
        print("1. Start game")
        print("2. Show Ranking")
        print("3. Exit")
        print("[!] Please input a value.")

    @staticmethod
    def start_game():
        """
        여기서 게임을 돌린다.
        :return:
        """
        Menu.show_ranking()

        loaders = Queries()  # 문제 로더로 쓰는 친구
        questions = loaders.load_game(db_file=Menu.db_file)

        game_result = InGame.when_the_question_is_given(questions)

        # 틀렸다면 걍 게임오버고
        if game_result == -1:
            return
        else:
            Menu.get_ranking(game_result)

    @staticmethod
    def show_ranking():
        """
        상위 5명만 랭킹 보여줌.
        :return:
        """
        players = Queries()  # 플레이어 데이터 가져오는 친구
        top5_rankers = players.get_top5_ranker(db_file=Menu.db_file)

        print("----- ---- --- ---- -----")
        print(" ----  HALL OF FAME ---- ")
        print("----- ---- --- ---- -----")
        for top5 in top5_rankers:
            print(top5)

    @staticmethod
    def exit_game():
        print("[!] bye!")
        sys.exit()

    @staticmethod
    def get_ranking(game_result):

        new_rankers = Queries()
        conn = new_rankers.create_connection(db_file=Menu.db_file)
        new_rankers.set_rankers_to_database(conn, game_result)


