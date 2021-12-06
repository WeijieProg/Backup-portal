class Maze:
    def __init__(self, maze_ID, arr):
        self.__maze_ID = maze_ID
        self.__map = arr
    def get_maze(self):
        return self.__map
    def get_maze_ID(self):
        return self.__maze_ID
    def update_maze(self, updatedMap):
        self.__map = updatedMap