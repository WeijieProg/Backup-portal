class Token:
    def __init__(self, token = None):
        self.__token = token

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token
    