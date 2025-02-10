from flask import Blueprint, render_template
from flask_login import login_required

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@main_routes.route('/meeting')
@login_required
def meeting():
    return render_template('meeting.html', title='Meeting')