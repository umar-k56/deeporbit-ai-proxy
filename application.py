from flask import Flask, redirect

application = Flask(__name__)
@application.route('/')
def index():
    return redirect('https://deeporbit-ai-e23fd19e8b29.herokuapp.com/')

