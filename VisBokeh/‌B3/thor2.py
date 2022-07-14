from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap

output_file('thor2.html')

data = pd.read_csv('thor_wwii.csv')

dataGrouped = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()
datasource = ColumnDataSource(dataGrouped)

countries = datasource.data['COUNTRY_FLYING_MISSION'].tolist()

p = figure(x_range=countries)

cm = factor_cmap(field_name='COUNTRY_FLYING_MISSION', palette=Spectral5, factors=countries)

cm = factor_cmap(field_name='COUNTRY_FLYING_MISSION', palette=Spectral5, factors=countries)
p.vbar(source=datasource, x='COUNTRY_FLYING_MISSION', color=cm, top='TOTAL_TONS', width=0.7)

h = HoverTool()
h.tooltips = [
    ('جمع',
     'جمع مواد منفجره تخریب قوی @TONS_HEاست و حجم مواد اتشزا @TONS_IC است و تعداد @TONS_FRAG قطعه منفجر شده است')
]
h.mode = 'vline'
p.add_tools(h)
show(p)