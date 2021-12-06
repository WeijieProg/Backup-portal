import logging
from flask import Blueprint, render_template, jsonify, request
from models import maze

"""
Creation of pregenerated mazes
"""
map1 = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0],
        [1,1,0,0,1,1,1,3],
        [2,0,0,0,0,0,0,0]]

map2 = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [2,1,1,1,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0],
        [1,1,0,0,1,1,1,3],
        [1,0,0,0,0,0,0,0]]

map3 = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,1,3,0,0],
        [1,1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0],
        [1,1,0,0,1,1,1,2],
        [1,0,0,0,0,0,0,0]]

maze_array = [maze.Maze("P1", map1), maze.Maze("P2", map2), maze.Maze("P3", map3)]
custom_mazes = []
custom_names = []

"""
function to return the maze array
"""
def get_mazes():
	mazes = maze_array + custom_mazes
	return mazes

"""
adding custom maze to array
"""
def create_custom_maze(name, arr):
	custom = maze.Maze(name, arr)
	custom_mazes.append(custom)
	custom_names.append(name)

"""
Clearing custom mazes
"""
def clear_custom_mazes():
	global custom_mazes
	global custom_names
	for i in custom_mazes:
		del i
	custom_names = []
	custom_mazes = []

"""
Routing for maze pages
"""
mazecreator_page = Blueprint("mazecreator_page", __name__)

@mazecreator_page.route('/MazeCreator', methods=['POST', 'GET'])
def maze_creator():
	if request.method == 'POST':
		data = request.get_json()
		create_custom_maze(data[0]['name'], data[1]['map'])
		result = {'processed':'true'}
		return jsonify(result)

	return render_template('mazecreator.html', data=custom_names)
