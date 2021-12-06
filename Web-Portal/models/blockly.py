class Blockly:
    def __init__(self, instructions=[]):
        self.__instructions = instructions

    def get_instructions(self, ):
        return self.__instructions

    def set_instructions(self, instructions):
        self.__instructions = instructions

