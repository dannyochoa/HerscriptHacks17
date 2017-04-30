from bokeh.resources import CDN
from bokeh.plotting import figure, output_file, show
from bokeh.embed import autoload_static
from bokeh.embed import components
import numpy as np

# output_file("line.html")
plot = figure(plot_width=1000, plot_height= 400)
plot.circle([1,2], [3,4])
# show(plot)
js, tag = autoload_static(plot, CDN, "./herscriptHacks/HerscriptHacks17/jss.js")


#print (js)

# print (tag)