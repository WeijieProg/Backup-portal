from flask import Blueprint, render_template, jsonify, request
from controllers import token_controller, connection_controller
from models.blockly import Blockly

dashboard_page = Blueprint('dashboard_page', __name__)
block_arr = []
obj = Blockly()

def get_instructions():
    instruction = block_arr
    return instruction

@dashboard_page.route('/dashboard', methods=['GET', 'POST'])
def blocklyPage():
    if request.method == 'POST':
        data = request.get_json()
        obj.set_instructions(data['instructions'])
        connection_controller.send_instruction(data['instructions'])
        result = {'processed': 'true'}
        return jsonify(result)
    return render_template('dashboard.html', data=get_instructions())

