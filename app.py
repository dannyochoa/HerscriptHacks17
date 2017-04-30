import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder='templates')


@app.route('/')
def login():
     return render_template('index.html')

# @app.route('/info', methods=['POST'])
# def info():
#     if request.methods=='POST':
#         if request.form['button'] == 'info':
#          return redirect(url_for('info'))
#     return render_template('index.html')

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
# =======
# @app.route('/')
# def login():
#     return render_template('index.html')
    
# @app.route('/', methods = ['POST'])
# def logged_process():
#     entered_id = request.form['id']
#     file = open("workerId.txt", "r") 
#     worker_id_list = file.readlines()
#     file.close()
#     file = open("secretaryId.txt", "r")
#     secretary_id_list = file.readlines()
#     file.close()
    
#     for id_num in secretary_id_list:
#         if(entered_id + '\n' == id_num):
#             return redirect(url_for('secretaryHomePage'))
#     for id_num in worker_id_list:
#         if(entered_id + '\n' == id_num):
#             return redirect(url_for('workerPage'))

# @app.route('/secretary')
# def secretaryHomePage():
#     file = open("comments.txt", 'r')
#     comments_entered = file.readlines()
#     file.close()
#     return render_template('secretary.html', comments_to_enter1= comments_entered[0],
#     comments_to_enter2= comments_entered[1],comments_to_enter3= comments_entered[2],
#     comments_to_enter4= comments_entered[3],comments_to_enter5= comments_entered[4])

# # process
# @app.route('/secretary', methods=['POST'])
# def secretary():
#     # get login parameters
#     name = request.form['name']
#     crew = request.form['crew']
#     worker_id = request.form['id']
#     # do login processing
#     if (request.form['submit'] == "login"):
#         file = open("workersInfo.txt", 'a')
#         file.write(worker_id + '\n')
#         file.write(name + '\n')
#         file.write(crew + '\n')
#         file.close()
#         file = open('workerId.txt', 'a')
#         file.write(worker_id + '\n')
#         file.close()
#         return redirect(url_for('secretary'))


# @app.route('/worker')
# def workerPage():
#     return render_template('workerPage.html')
    
# @app.route('/worker', methods=['POST'])
# def workerInput():
#     comment = request.form['comment']
#     if (request.form['submit'] == "login"):
#         file = open("comments.txt" , 'a')
#         file.write("<worker id>: " + comment + '\n')
#         file.close()
#         return redirect(url_for('workerInput'))
    
# >>>>>>> 7140abe3b46267a86962cfdf686a7bd6bef12cc7


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )