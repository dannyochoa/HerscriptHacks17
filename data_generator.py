from datetime import datetime
import time
import random as rand


def gen_liter(data):
    if data == 1:
        num = rand.randint(rand.randint(80, 100), rand.randint(190, 210))
    if data == 2:
        num = rand.randint(rand.randint(90, 120), rand.randint(200, 220))
    if data == 3:
        num = rand.randint(120, 220)
    if data == 4:
        num = rand.randint(180, 280)
    if data == 5:
        num = rand.randint(190, 290)
    if data == 6:
        num = rand.randint(210, 310)
    if data == 7:
        num = rand.randint(230, 330)
    if data == 8:
        num = rand.randint(230, 330)
    if data == 9:
        num = rand.randint(190, 290)
    if data == 10:
        num = rand.randint(160, 260)
    if data == 11:
        num = rand.randint(140, 240)
    if data == 12:
        num = rand.randint(110, 210)
    return num


def gen_energy(data):
    if data == 1:
        num = rand.randint(500, 1000)
    if data == 2:
        num = rand.randint(600, 1100)
    if data == 3:
        num = rand.randint(700, 1200)
    if data == 4:
        num = rand.randint(1000, 1500)
    if data == 5:
        num = rand.randint(1100, 1600)
    if data == 6:
        num = rand.randint(1200, 1700)
    if data == 7:
        num = rand.randint(1300, 1800)
    if data == 8:
        num = rand.randint(1300, 1800)
    if data == 9:
        num = rand.randint(1100, 1600)
    if data == 10:
        num = rand.randint(900, 1400)
    if data == 11:
        num = rand.randint(700, 1000)
    if data == 12:
        num = rand.randint(500, 1000)
    return num


def convert_todatetime(data):
    my_date = datetime.strptime(str(data), "%m")
    return my_date.strftime("2017-%m-01")


def convert_totimestamp(data):
    my_date = datetime.strptime(str(data), "%Y-%m-%d")
    d = datetime.date(my_date)

    unixtime = time.mktime(d.timetuple())
    return unixtime
