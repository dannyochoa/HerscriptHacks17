import pandas as pd
from datetime import datetime
import numpy as np
import random as rand
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from bokeh.models import HoverTool
import math


def gen_liter(datetime):
    data = int(convert_tonum(datetime))
    # data = dat/etime
    # df.loc[(df['date'] == 1), 'liters'] = np.random.randint(0,100)
    num = 0
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


def gen_energy(datetime):
    data = int(datetime)
    # df.loc[(df['date'] == 1), 'liters'] = np.random.randint(0,100)
    num = 0
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


def convert_tonum(data):
    my_date = datetime.strptime(data, "%Y-%m-%d")
    return my_date.strftime("%m")

def convert_todatetime(data):
    my_date = datetime.strptime(data, "%m")
    return my_date.strftime("2017-%m-00")


df = pd.read_csv('Data/datetime.csv', header=0, names=['date'])

# date = pd.date_range(start='1-01-17', end='12-01-17', freq='MS')
df['month'] = df['date'].apply(convert_tonum)

df['liter'] = df['date'].apply(gen_liter)

df_liter = pd.DataFrame({'liter': df['liter'], 'date': df['date'], 'month': df['month']},
                        columns=['liter', 'date', 'month'])

df_liter.sort_values('month', inplace=True)

df_liter_grouped = df_liter.groupby('month').mean()
df_liter_grouped['datetime'] = df_liter_grouped.index.values

df_liter_grouped['datetime'] = df_liter_grouped['datetime']. apply(convert_todatetime)
# df_liter_grouped['month2'] = df_liter_grouped.index

output_file("line.html")

p = figure(plot_width=1000, plot_height=400, title="Water usage L/kg/y")

# add a circle renderer with a size, color, and alpha
print(df_liter_grouped)

# p.circle(df['month'], df['liter'], size=20, color="navy", alpha=0.5)
p.line(df_liter_grouped['datetime'], df_liter_grouped['liter'])

p.xaxis[0].formatter=DatetimeTickFormatter(
        hours=["%B"],
        days=["%B"],
        months=["%B"],
        years=["%B"],
    )

p.xaxis.axis_label = "Month"
p.yaxis.axis_label = "L/kg"

# show the results
show(p)
# plt.show()

# print(df)
# gen_data(df)
