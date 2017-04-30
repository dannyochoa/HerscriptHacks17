# Author: Joshua Saavedra
# Date: 4/29/17

import pandas as pd
import numpy as np

from bokeh.charts import HeatMap, output_file, show
from bokeh.layouts import column, gridplot

# These lists are randomized to simulate data
list1 = np.random.uniform(1, 10, 20)
list2 = np.random.uniform(1, 10, 20)

# This dictionary was created to  hold our 'data'
fruits = { # This 'fruit' key holds a list of fruits, for know it is  4x5
	  'fruit'        : ['apples', 'apples', 'apples', 'apples', 'apples',
                    	    'pears', 'pears', 'pears', 'pears', 'pears',
                            'bananas', 'bananas', 'bananas', 'bananas', 'bananas',
			    'mango', 'mango', 'mango', 'mango', 'mango'],
          'fruit_count1' : list1,
	  'fruit_count2' : list2,
	  # This 'year' key holds a list of years multiplied by our amount of DIFFERENT fruits
          'year'	 : [2009, 2010, 2011, 2012, 2013]*4}
# This line changes the contents of 'year' from int to string
fruits['year'] = [str(yr) for yr in fruits['year']]

# These lines create our heat maps
hm  = HeatMap(fruits, y='year', x='fruit', values='fruit_count1', stat=None)
ohm = HeatMap(fruits, y='year', x='fruit', values='fruit_count2', stat=None)

# Output section
output_file("heatmap.html", title="heatmap.py example")
show(column(gridplot(ohm, hm, ncols=2, plot_width=400, plot_height=400)))
