# Author: Joshua Saavedra
# Date: 4/29/17
# Note: Examples are heavily used for this script

import pandas as pd
import numpy as np
from bokeh.charts import HeatMap, output_file, show
from bokeh.layouts import column, gridplot

# This line reads in from a csv file
#df = pd.read_csv('test.csv')

# The stuff within ths boundry
############################################################################################
# Standard size for each data list
SIZE = 5

# This function will fill in a passed in list
def fill_list(stri, the_list = [], *args):
	for i in range(SIZE):
		the_list.append(stri)
	return the_list

# These lists are representations of objects, in this instance, fruit
apples  = []
bananas = []
pears   = []
mangos  = []

fill_list("apples", apples)
fill_list("bananas", bananas)
fill_list("pears", pears)
fill_list("mangos", mangos)

fruit_basket = apples + bananas + pears + mangos

# These lists are randomized to simulate data
data_list = np.random.uniform(1, 10, len(fruit_basket))

# List of years
years = [2009, 2010, 2011, 2012, 2013]

# This line changes the contents of 'year' from int to string
years = [str(yr) for yr in years]

# This dictionary was created to  hold our 'data'
fruits = {'fruit'    : fruit_basket,
	  'year'     : years*4,
          'the_data' : data_list}

# A data frame is created
df = pd.DataFrame.from_dict(fruits)

# The columns are reorganized 
df['temp'] = df['year']
df['year'] = df['the_data']
df['the_data'] = df['temp']
# The 'temp' column is deleted
del df['temp']
# The columns are properly renamed
df.columns = ['fruit', 'year', 'data']
############################################################################################

# The information is printed
print(df.index)
print(df.columns)
print(df)

# The heatmap is created
hm = HeatMap(df) #, x=df.name, y=df.iloc[1], values=df.iloc[2], stat=None)

# Output section
output_file("heatmap.html", title="heatmap.py example")
show(hm)

