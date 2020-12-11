import os
import flask
from flask import Flask, render_template, redirect, jsonify
import api
from flask import request
import time
import datetime
from flask import redirect, url_for
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def main_page():
    return render_template("index.html")
@app.route('/documentation')
def docs():
    return "docs"
@app.route('/about_me')
def about_me():
    args = request.args
    if 'login' in args and 'password' in args:
        login = args["login"]
        password = args["password"]
    else:
        return jsonify('''{"error" : true, "error_text" : "login and password is required"}''')
    a = api.about_me(login, password)
    return str(a).encode('utf-8')
@app.route('/all_marks')
def all_marks():
    args = request.args
    if 'login' in args and 'password' in args:
        login = args["login"]
        password = args["password"]
    else:
        return jsonify('''{"error" : true, "error_text" : "login and password is required"}''')
    if 'period' in args:
        period = args['period']
    else:
        return jsonify('''{"error" : true, "error_text" : "period is required"}''')
    a = api.all_marks(login, password, period)
    return str(a).encode('utf-8')
@app.route('/daily')
def alll_marks():
    args = request.args
    if 'login' in args and 'password' in args:
        login = args["login"]
        password = args["password"]
    else:
        return jsonify('''{"error" : true, "error_text" : "login and password is required"}''')
    if 'day' in args and 'year' in args and 'month' in args:
        day = args['day']
        year = args['year']
        month = args['month']
        s = f"{day}/{month}/{year}"
        unix_day = int(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
    else:
        return jsonify('''{"error" : true, "error_text" : "day, year, month is required"}''')
    a = api.day_info(login, password, unix_day)
    return str(a).encode('utf-8')

@app.route('/documentation/about_me')
def asd():
    return render_template('about.html')

@app.route('/documentation/day_info')
def asddd():
    return render_template('day.html')

@app.route('/documentation/all_marks')
def asdd():
    return render_template('period.html')

def main():
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
