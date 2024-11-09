from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

get_timezone = __import__('7-app').get_timezone


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """Get the current time based on the inferred timezone"""
    user_timezone = get_timezone()
    timezone = pytz.timezone(user_timezone)
    current_time = datetime.now(timezone).strftime('%b %d, %Y, %I:%M:%S %p')
    
    return render_template('index.html', current_time=current_time)