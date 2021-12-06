import secrets, logging
from models.token import Token
from flask import Blueprint, render_template

auth_token = Token()

def generate_token():
    auth_token.set_token(secrets.token_urlsafe(16))
    # debugging
    # logging.debug(auth_token.get_token())

    return auth_token.get_token()

def get_token():
    return auth_token.get_token()

def check_token():
    if auth_token.get_token() != None:
        return True
    else:
        generate_token()

def verify_token(token_from_car):
    # logging.debug(self.auth_token.get_code())
    # logging.debug(code)
    return secrets.compare_digest(token_from_car, auth_token.get_token())

def clear_token():
    auth_token.set_token(None)