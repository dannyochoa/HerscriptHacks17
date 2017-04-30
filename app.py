import os
from flask import Flask, render_template, request, url_for, redirect
from roster import get_roster, write_to
from bokeh.resources import CDN
from bokeh.plotting import figure, output_file, show
from bokeh.embed import autoload_static
from bokeh.embed import components
import numpy as np

people = get_roster("Data/roster.csv")

app = Flask(__name__, template_folder='template')
entered_id = ""
QA = "Nothing has been inputed by the secratary Yet"
crew_comment = "Nothing has been inputed by the secratary Yet"
crew1 = 8
crew2 = 3
crew3 = 1

@app.route('/')
def login():
    plot = figure(plot_width=1000, plot_height= 400)
    plot.circle([1,2], [3,4])
    script, div = components(plot)

    #return render_template('line_test.html', script=script, div=div)
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
        if(entered_id == '1234'):
            return redirect(url_for('secretaryHomePage'))
        elif(entered_name == people[int(entered_id)][0]):
            return redirect(url_for('workerPage'))
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
    name = request.form['name']
    crew = request.form['crew']
    worker_id = request.form['id']
    if (request.form['submit'] == "login"):
        write_to(worker_id, name, int(crew), "Data/roster.csv")
        return redirect(url_for('secretary'))

@app.route('/worker')
def workerPage():
    return render_template('workerPage.html', worker_id = entered_id, worker_name = people[int(entered_id)][0], 
    worker_crew = people[int(entered_id)][1], qa_entered = QA, comCrew = crew_comment, c1 = crew1, c2 = crew2, c3 = crew3)
    
@app.route('/worker', methods=['POST'])
def workerInput():
    comment = request.form['comment']
    if (request.form['submit'] == "login"):
        current_comment = people[int(entered_id)][0] + ": " + comment + '\n'
        file = open("comments.txt" , 'r')
        comment_list = file.readlines()
        file.close()
        file = open("comments.txt" , "w")
        file.write(current_comment)
        for com in comment_list:
            file.write(com)
        file.close()
        return redirect(url_for('workerInput'))
        
        
@app.route('/officeInfo')
def officeInfo():
    return render_template('officeInfo.html')
    
@app.route('/officeInfo', methods = ['POST'])
def enterOfficeInfo():
    global QA, crew_comment, crew1, crew2, crew3
    QA = request.form['qa']
    crew_comment = request.form['crew_comment']
    crew1 = request.form['crew1']
    crew2 = request.form['crew2']
    crew3 = request.form['crew3']
    if (request.form['submit'] == "plot"):
        return redirect(url_for('officeInfo'))
    

if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )