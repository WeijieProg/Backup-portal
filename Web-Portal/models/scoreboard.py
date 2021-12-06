import pandas as pd
from datetime import datetime


class Scoreboard:
    def __init__(self, data=None, score=[], name=[], date=[]):
        self.__date = date
        self.__data = data
        self.__score = score
        self.__name = name

    def set_data(self, data):
        self.__data = pd.read_csv(data)

    def get_data(self):
        return self.__data

    def set_date(self, date):
        self.__date.clear()
        for i in range(len(date)):
            self.__date.append(date.iloc[i:i+1, 1:2])
            if type(self.__date[i]) is not str:
                self.__date[i] = self.__date[i].to_string(index=False, header=False)

    def get_date(self):
        return self.__date

    def set_name(self, name):
        self.__name.clear()
        for i in range(len(name)):
            self.__name.append(name.iloc[i:i + 1, 0:1])
            if type(self.__name[i]) is not str:
                self.__name[i] = self.__name[i].to_string(index=False, header=False)

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score.clear()
        for i in range(len(score)):
            self.__score.append(score.iloc[i:i+1, 2:3])
            if type(self.__score[i]) is not str:
                self.__score[i] = self.__score[i].to_string(index=False, header=False)

    def get_score(self):
        return self.__score
