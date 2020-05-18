# package import
import hashlib
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime

# local import
from app import db
from app.models.attendance import AttendanceModel
from app.helpers import auth

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route('/attendance/report', methods=['GET', 'POST'])
@login_required
def report():
    if request.method == 'GET':
        return render_template('attendance/report.html', current_user=current_user)
    else:
        user_id = current_user.id
        current_time = request.form['current_time']
        current_time = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
        report_type = request.form['report_btn']
        if report_type == 'in':
            last_attendance = AttendanceModel.get_recent_by_user_id(user_id)
            # Check whether or not the user has reported in
            if last_attendance and last_attendance.time_in.date() == current_time.date():
                message = 'You have reported in today!'
                return render_template('attendance/report.html', current_user=current_user, message=message)

            attendance = AttendanceModel(
                user_id = user_id,
                time_in = current_time
            )

            try:
                attendance.insert()
                db.session.commit()
            except:
                db.session.rollback()
                message = 'Error while reporting attendance, please try again'
            
            message = 'Thank you for reporting your attendance'
            return render_template('attendance/report.html', current_user=current_user, message=message)
        else:
            last_attendance = AttendanceModel.get_recent_by_user_id(user_id)
            # Check whether or not the user has reported in
            if last_attendance is None\
                or (last_attendance and last_attendance.time_in.date() != current_time.date()):
                message = 'You haven\'t reported in today!'
                return render_template('attendance/report.html', current_user=current_user, message=message)
            # Check whether or not the user has reported out
            if last_attendance and last_attendance.time_out\
                and last_attendance.time_out.date() == current_time.date():
                message = 'You have reported out today!'
                return render_template('attendance/report.html', current_user=current_user, message=message)

            try:
                # Update time out
                last_attendance.time_out = current_time
                db.session.commit()
            except:
                db.session.rollback()
                message = 'Error while reporting attendance, please try again'
            
            message = 'Thank you for reporting your attendance, take care on your way home'
            return render_template('attendance/report.html', current_user=current_user, message=message)

@attendance_bp.route('/attendance/history')
@login_required
def history():
    attendances = AttendanceModel.get_by_user_id(current_user.id)
    return render_template('attendance/history.html', current_user=current_user, attendances=attendances)
