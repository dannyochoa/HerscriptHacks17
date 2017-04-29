import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder='template')


@app.route('/login/<int:num>')
def login():
    return render_template('login.html')


# process
@app.route('/login', methods=['POST'])
def login_process():
    # get login parameters
    name = request.form['name']
    password = request.form['password']
    # do login processing
    return redirect(url_for('logged_in', name=name))


@app.route('/logged_in')
def logged_in():
    return render_template('logged_in.html', name=request.args.get('name'))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )