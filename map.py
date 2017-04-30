import numpy as np
from bokeh.charts import HeatMap, output_file, show
from bokeh.layouts import column, gridplot
from bokeh.embed import components


# Standard size for each data list

def get_heatmap():
    SIZE = 5

    # This function will fill in a passed in list
    def fill_list(stri, the_list=[], *args):
        for i in range(SIZE):
            the_list.append(stri)
        return the_list

    # This function produces a list filled with random numbers
    def random_data():
        return np.random.uniform(1, 100, len(list_of_resources))

    # These lists are representations of objects, in this instance, fruit
    water = []
    fruits = []
    veggies = []
    soil = []

    # These lines fill the lists
    fill_list("Water", water)
    fill_list("Fruits", fruits)
    fill_list("Vegetables", veggies)
    fill_list("Soil", soil)

    # This line combines all of the lists into one
    list_of_resources = water + fruits + veggies + soil

    # List of years
    years = [2009, 2010, 2011, 2012, 2013]

    # This line changes the contents of 'year' from int to string
    years = [str(yr) for yr in years]

    # This dictionary was created to  hold our 'data'
    statistics = {'resources': list_of_resources,
                  'year': years * 4,
                  'data1': random_data(),
                  'data2': random_data(),
                  'data3': random_data(),
                  'data4': random_data()}

    # The heatmaps are created
    hm01 = HeatMap(statistics, x='resources', y='year', values='data1', stat=None, title="Field 1")
    hm02 = HeatMap(statistics, x='resources', y='year', values='data2', stat=None, title="Field 2")
    hm03 = HeatMap(statistics, x='resources', y='year', values='data3', stat=None, title="Field 3")
    hm04 = HeatMap(statistics, x='resources', y='year', values='data4', stat=None, title="Field 4")

    # Output section
    output_file("heatmap.html", title="Field Resource Usage")
    heat_list = [hm01, hm02, hm03, hm04]
    p = column(gridplot(hm01, hm02, hm03, hm04, ncols=2, plot_width=500, plot_height=500))
    script_div = components(p)

    return script_div
