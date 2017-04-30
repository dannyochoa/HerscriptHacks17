import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from bokeh.models import HoverTool
from data_generator import convert_todatetime, convert_totimestamp, gen_liter

if __name__ == "__main__":
    df = pd.read_csv('Data/randmonth.csv', header=0, names=['month_num'])

    date = pd.date_range(start='1-01-17', end='12-01-17', freq='MS')
    df['liter'] = df['month_num'].apply(gen_liter)
    df['datetime'] = df['month_num'].apply(convert_todatetime)
    df['timestamp'] = df['datetime'].apply(convert_totimestamp)

    df_liter = pd.DataFrame({'liter': df['liter'], 'month_num': df['month_num'], 'datetime': df['datetime'],
                             'timestamp': df['timestamp']}, columns=['liter', 'month_num', 'timestamp'])
    df_liter.sort_values('month_num', inplace=True)
    df_liter_grouped = df_liter.groupby('month_num').mean()
    df_liter_grouped['datetime'] = date
    output_file("line.html")

    df['timestamp'] = df['timestamp'].apply(lambda x: (x * 1000))
    df_liter_grouped['timestamp'] = df_liter_grouped['timestamp'].apply(lambda x: (x * 1000))

    p = figure(plot_width=1000, plot_height=400, title="Water usage L/kg/y")
    p.circle(df['timestamp'], df['liter'], size=20, color="navy", alpha=0.5)
    p.line(df_liter_grouped['timestamp'], df_liter_grouped['liter'])
    p.xaxis[0].formatter = DatetimeTickFormatter(months="%b")

    p.xaxis.axis_label = "Month"
    p.yaxis.axis_label = "L/kg"

    show(p)
