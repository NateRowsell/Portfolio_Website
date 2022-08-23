from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/')
def auth():
    return "<h1>auth</h1>"