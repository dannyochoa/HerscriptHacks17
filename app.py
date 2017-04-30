import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder='templates')


# @app.route('/', methods=['POST'])
# def login():
#      if request.methods=='POST':
#         if request.form['button'] == 'info':
#          return redirect(url_for('info'))
#      return render_template('index.html')

@app.route('/info', methods=['POST'])
def info():
   
    return render_template('index.html')

# process
# @app.route('/index', methods=['POST'])
# def login_process():
#     # get login parameters
#     name = request.form['Email']
#     password = request.form['Password']
#     # do login processing
#     return redirect(url_for('index', name=name))


# @app.route('/logged_in')
# def logged_in():
#     return render_template('logged_in.html', name=request.args.get('Email'))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )