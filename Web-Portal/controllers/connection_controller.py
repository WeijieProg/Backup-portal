from models.connection import Connection
from controllers import connection_controller, token_controller, maze_controller
from flask import Flask, render_template, request, Blueprint
import requests

conn = Connection()

"""
setting IP and port for connection to robotic car
"""
def connect_to_car(ip, port):
    conn.set_ip(ip)
    conn.set_port(port)


"""
get IP and port for the robotic car
"""
def get_address():
    return {'ip': conn.get_ip(), 'port': conn.get_port()}


"""
clear IP and port
"""
def disconnect():
    conn.set_ip("0.0.0.0")
    conn.set_port("0")


"""
Send instructions
"""
def send_instruction(instructions):
    cleaned_instructions = []
    index = 0;
    count = 0
    count2 = 0
    print(instructions)
    for instruction in instructions:
        if instruction == 'Forward' or instruction == '  Forward' or instruction == '}\nForward':
            cleaned_instructions.append('f')
        elif instruction == 'Left' or instruction == '  Left' or instruction == '}\nLeft':
            cleaned_instructions.append('l')
        elif instruction == 'Right' or instruction == '  Right' or instruction == '}\nRight':
            cleaned_instructions.append('r')
        elif 'for' in instruction:
            if instruction.count('for') != 1:
                while count != instruction.count('for'):
                    while instruction[index:index+2] != '< ':
                        index += 1
                    index += 2
                    if count == 0:
                        count2 = int(instruction[index:index+1])
                    else:
                        count2 *= int(instruction[index:index+1])
                    count += 1
            if instruction[28:29] != ' ':
                if "Forward" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('F' + instruction[28:29])
                    else:
                        cleaned_instructions.append('F' + str(count2))
                elif "Left" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('L' + instruction[28:29])
                    else:
                        cleaned_instructions.append('L' + str(count2))
                elif "Right" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('R' + instruction[28:29])
                    else:
                        cleaned_instructions.append('R' + str(count2))
            else:
                if "Forward" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('F' + instruction[28:29])
                    else:
                        cleaned_instructions.append('F' + str(count2))
                elif "Left" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('L' + instruction[28:29])
                    else:
                        cleaned_instructions.append('L' + str(count2))
                elif "Right" in instruction:
                    if count2 == 0:
                        cleaned_instructions.append('R' + instruction[28:29])
                    else:
                        cleaned_instructions.append('R' + str(count2))

    address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
    testDat = {'ISN': 1}

    count = 1
    for instruction in cleaned_instructions:
        testDat['D' + str(count)] = instruction
        count += 1

    testDat['TOK'] = token_controller.get_token()
    testDat['E'] = '#'

    # r = "200"
    r = requests.post(address, testDat)
    print(token_controller.get_token())
    print(r.status_code)

    # if r == "200":
    if r.status_code == 200:
        # r = token_controller.get_token()
        r = requests.get(address, params={"type": "T"})
        if token_controller.verify_token(r.text):
            print("Verified")


"""
Routing for maze pages
"""
connection_page = Blueprint('connection_page', __name__)


@connection_page.route('/connection', methods=['GET', 'POST'])
def connectionPage():
    token_controller.check_token()
    if request.method == 'POST':
        connect_to_car(request.form['ipInput'], request.form['portInput'])

        address = "http://" + conn.get_ip() + ":" + conn.get_port() + "/"
        testDat = {'ISN': 0, 'TOK': token_controller.get_token(), 'E': '#'}
        #r = "200"
        r = requests.post(address, testDat)
        print(token_controller.get_token())
        print(r.status_code)

        #if r == "200":
        if r.status_code == 200:
            #r = token_controller.get_token()
            r = requests.get(address, params={"type": "T"})
            print(r.text)
            print(token_controller.get_token())
            if token_controller.verify_token(r.text):
                print("Verified")
                return render_template('dashboard.html')

    disconnect()
    conn_details = connection_controller.get_address()
    token_controller.clear_token()
    maze_controller.clear_custom_mazes()
    return render_template('connection.html', address=conn_details)
