from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("StartDate", validators=[DataRequired()])
    start_time = TimeField("Start Time", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    end_time = TimeField("End Time", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private")
    submit = SubmitField("Add Appointment")
