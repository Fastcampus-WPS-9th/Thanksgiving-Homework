# -*- coding:utf-8 -*-
#
# 유저 정보를 여기에 잠시담고
# 디비에 차후 update할 때 참조.

import sqlite3
from sqlite3 import Error


class Players:

    def __init__(self, user_id, user_name):
        self.__life = 2
        self.__score = 0
        self.user_id = user_id
        self.user_name = user_name

    @property
    def current_score(self):
        """ 점수에 대한 getter """
        return self.__score

    @current_score.setter
    def current_score(self, achieved_score):
        """ 점수에 대한 setter. 문제를 맞췄으니 점수를 더해줌 """
        self.__score += achieved_score

    @property
    def current_life(self):
        """ 라이프에 대한 getter """
        return self.__life

    @current_life.setter
    def current_life(self, life):
        """라이프에 대한 getter. 문제를 틀렸으니 라이프를 깜 """
        self.__life -= life

