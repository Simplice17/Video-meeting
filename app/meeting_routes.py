from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Meeting, db
from app.utils import generate_meeting_id

meeting_routes = Blueprint('meeting_routes', __name__)

@meeting_routes.route('/create_meeting', methods=['GET', 'POST'])
@login_required
def create_meeting():
    if request.method == 'POST':
        meeting_id = generate_meeting_id()
        meeting = Meeting(meeting_id=meeting_id, host_id=current_user.id)
        db.session.add(meeting)
        db.session.commit()
        flash('Meeting created successfully!', 'success')
        return redirect(url_for('meeting_routes.meeting', meeting_id=meeting_id))
    return render_template('create_meeting.html', title='Create Meeting')

@meeting_routes.route('/meeting/<meeting_id>')
@login_required
def meeting(meeting_id):
    meeting = Meeting.query.filter_by(meeting_id=meeting_id).first()
    if not meeting:
        flash('Meeting not found!', 'danger')
        return redirect(url_for('main_routes.home'))
    return render_template('meeting.html', title='Meeting', meeting_id=meeting_id)

@meeting_routes.route('/join_meeting', methods=['GET', 'POST'])
@login_required
def join_meeting():
    if request.method == 'POST':
        meeting_id = request.form.get('meeting_id')
        meeting = Meeting.query.filter_by(meeting_id=meeting_id).first()
        if not meeting:
            flash('Invalid meeting ID!', 'danger')
            return redirect(url_for('meeting_routes.join_meeting'))
        return redirect(url_for('meeting_routes.meeting', meeting_id=meeting_id))
    return render_template('join_meeting.html', title='Join Meeting')