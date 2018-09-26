# -*- coding:utf-8 -*-
#
# 문제는 여기서 임포트하고
# 문제들을 딕셔너리로 리턴함.

import sqlite3
from sqlite3 import Error


class Queries:
    def __init__(self):
        self.question = {}
        self.__answer = None
        self.__score_points = None

    def load_game(self, db_file):
        '''
        게임 데이터 로드
        :param db_file:
        :return:
        '''
        conn = self.create_connection(db_file)
        qna = self.get_question_data_from_database(conn)

        return qna

    def get_top5_ranker(self, db_file):
        '''
        랭커 데이터 로드
        :param db_file:
        :return:
        '''
        conn = self.create_connection(db_file)
        top5_ranker = self.get_top_rankers_from_database(conn)

        return top5_ranker

    @staticmethod
    def create_connection(db_file):
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)

            return conn
        except Error as e:
            print(e)

    @staticmethod
    def get_question_data_from_database(conn):
        '''
        최대 8문제 랜덤으로 뽑음. 테이블 전체를 딕셔너리 리턴.
        :param conn:
        :return:
        '''
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT question_details, answer_number "
                "FROM questions_1vs100 "
                "ORDER BY random() "
                "LIMIT 8;"
            )

            qna = cur.fetchall()

            return qna

        except Error as e:
            print(e)

        finally:
            conn.close()

    @staticmethod
    def get_top_rankers_from_database(conn):
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT player_id, player_name, achieved_score "
                "FROM players_1vs100 "
                "ORDER BY achieved_score DESC;"
            )

            top5 = cur.fetchall()

            return top5

        except Error as e:
            print(e)

        finally:
            conn.close()

    @staticmethod
    def set_rankers_to_database(conn, game_result):
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO players_1vs100 "
                "(player_id, player_name, player_life, achieved_score, is_all_cleared) "
                "VALUES "
                "(?, ?, ?, ?, ?);"
                , game_result
            )

            conn.commit()

        except Error as e:
            print(e)

        finally:
            conn.close()