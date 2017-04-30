import os
from flask import Flask, render_template, request, url_for, redirect
from roster import get_roster

people = get_roster("Data/roster.csv")

app = Flask(__name__, template_folder='template')
entered_id = ""

@app.route('/')
def login():
    return render_template('index.html')
    
@app.route('/', methods = ['POST'])
def logged_process():
    global entered_id
    entered_id = request.form['id']
    entered_name = request.form['name']
    file = open("secretaryId.txt", "r")
    secretary_id_list = file.readlines()
    file.close()
    if (request.form['submit'] == "login"):
        if(entered_name == people[int(entered_id)][0]):
            return redirect(url_for('workerPage'))
        else:
            for id_num in secretary_id_list:
                if(entered_id + '\n' == id_num):
                    return redirect(url_for('secretaryHomePage'))
                else:
                    return redirect(url_for('logged_process'))
    if (request.form['submit'] == "info"):
        return redirect(url_for('information'))
        
@app.route('/info')
def info():
    return render_template('info.html')
    
@app.route('/secretary')
def secretaryHomePage():
    file = open("comments.txt", 'r')
    comments_entered = file.readlines()
    file.close()
    return render_template('secretary.html', comments_to_enter1= comments_entered[0],
    comments_to_enter2= comments_entered[1],comments_to_enter3= comments_entered[2],
    comments_to_enter4= comments_entered[3],comments_to_enter5= comments_entered[4])

# process
@app.route('/secretary', methods=['POST'])
def secretary():
    # get login parameters
    name = request.form['name']
    crew = request.form['crew']
    worker_id = request.form['id']
    # do login processing
    if (request.form['submit'] == "login"):
        file = open("workersInfo.txt", 'a')
        file.write(worker_id + '\n')
        file.write(name + '\n')
        file.write(crew + '\n')
        file.close()
        file = open('workerId.txt', 'a')
        file.write(worker_id + '\n')
        file.close()
        return redirect(url_for('secretary'))


@app.route('/worker')
def workerPage():
    return render_template('workerPage.html', worker_id = entered_id, worker_name = people[int(entered_id)][0], worker_crew = people[int(entered_id)][1])
    
@app.route('/worker', methods=['POST'])
def workerInput():
    comment = request.form['comment']
    if (request.form['submit'] == "login"):
        file = open("comments.txt" , 'a')
        file.write("<worker id>: " + comment + '\n')
        file.close()
        return redirect(url_for('workerInput'))
    

if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )