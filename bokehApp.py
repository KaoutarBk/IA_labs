import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Select
from bokeh.io import curdoc
from bokeh.layouts import row

df = pd.read_csv("./music_dataset/data.csv")
CarlWoitschachData = df[df['artists'].str.contains('Carl Woitschach')]
source = ColumnDataSource(CarlWoitschachData)
print(source)