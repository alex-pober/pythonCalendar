from flask import Blueprint, render_template
import os
import psycopg2
from app.forms import AppointmentForm

bp = Blueprint('main', __name__, url_prefix='/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route("/")
def main():
    form = AppointmentForm()
    # Create a psycopg2 connection with the connection parameters
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        # Create a cursor from the connection
        with conn.cursor() as curs:
            curs.execute(
                """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime;
                """
            )
            # Fetch all of the records
            rows = curs.fetchall()

    return render_template("main.html", rows=rows, form=form)
