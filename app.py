import os
from flask import Flask, render_template, request, url_for, redirect
from roster import get_roster, write_to
from ResourceData import get_tags
from bokeh.resources import INLINE
from map import get_heatmap

people = get_roster("Data/roster.csv")

app = Flask(__name__, template_folder='template')

entered_id = ""
QA = "Nothing has been inputed by the secretary Yet"
crew_comment = "Nothing has been inputed by the secretary Yet"
crew1 = 8
crew2 = 3
crew3 = 1


@app.route('/')
def login():

    # return render_template('line_test.html', script=script, div=div)
    return render_template('index.html')


@app.route('/', methods=['POST'])
def logged_process():
    global entered_id
    entered_id = request.form['id']
    entered_name = request.form['name']
    file = open("secretaryId.txt", "r")
    secretary_id_list = file.readlines()
    file.close()
    try:
        if (request.form['submit'] == "login"):
            if (entered_id == '1234'):
                return redirect(url_for('secretaryHomePage'))
            elif (entered_name == people[int(entered_id)][0]):
                return redirect(url_for('workerPage'))
            else:
                return redirect(url_for('logged_process'))
    except:
        return redirect(url_for('logged_process'))

    if (request.form['submit'] == "info"):
        return redirect(url_for('information'))


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/secretary')
def secretaryHomePage():
    # plot = figure(plot_width=1000, plot_height=400)
    # plot.circle([1, 2], [3, 4])

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = get_tags("Data/randmonth.csv")
    script2, div2 = get_heatmap()

    file = open("comments.txt", 'r')
    comments_entered = file.readlines()
    file.close()
    return render_template('secretary.html',
                           plot_script=script,
                           plot_div=div, plot_script2=script2, plot_div2 = div2,
                           js_resources=js_resources,
                           css_resources=css_resources)


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
    return render_template('workerPage.html', worker_id=entered_id, worker_name=people[int(entered_id)][0],
                           worker_crew=people[int(entered_id)][1], qa_entered=QA, comCrew=crew_comment, c1=crew1,
                           c2=crew2, c3=crew3 ,dm = people[int(entered_id)][2])


@app.route('/worker', methods=['POST'])
def workerInput():
    comment = request.form['comment']
    if (request.form['submit'] == "login"):
        current_comment = people[int(entered_id)][0] + " ID Number " + entered_id + ": " + comment + '\n'
        file = open("comments.txt", 'r')
        comment_list = file.readlines()
        file.close()
        file = open("comments.txt", "w")
        file.write(current_comment)
        for com in comment_list:
            file.write(com)
        file.close()
        return redirect(url_for('workerInput'))

@app.route('/officeReply')
def officeReply():
    file = open("comments.txt", 'r')
    comments_entered = file.readlines()
    file.close()
    return render_template('officeReply.html',  comments_to_enter1=comments_entered[0],
                           comments_to_enter2=comments_entered[1], comments_to_enter3=comments_entered[2],
                           comments_to_enter4=comments_entered[3], comments_to_enter5=comments_entered[4])
    
@app.route('/officeReply', methods = ['POST'])
def reply():
    worker_id = request.form['worker_id']
    message = request.form['message']
    people[int(worker_id)][2] = message
    if (request.form['submit'] == "login"):
        return redirect(url_for('officeReply'))


@app.route('/officeInfo')
def officeInfo():
    return render_template('officeInfo.html')


@app.route('/officeInfo', methods=['POST'])
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
