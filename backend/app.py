# import sys
# sys.path.append('C:/Users/phili/adc-forms')
from flask import Flask, request, redirect
from .db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome!<h1>'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO adc_members (membership_id, first_name, last_name, email, address, phone_number, local_government, polling_unit)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data['membership_id'],
        data['first_name'],
        data['last_name'],
        data['email'],
        data['address'],
        data['phone_number'],
        data['local_government'],
        data['polling_unit']
    ))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("https://wondrous-fenglisu-67c8a9.netlify.app/thank-you.html")

if __name__ == '__main__':
    app.run(debug=True)