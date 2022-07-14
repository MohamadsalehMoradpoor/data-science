from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap

output_file('thor3.html')

data = pd.read_csv('thor_wwii.csv')
data = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]

dataGrouped = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()
datasource = ColumnDataSource(dataGrouped)

countries = datasource.data['COUNTRY_FLYING_MISSION'].tolist()

p = figure(x_range=countries)

p.vbar_stack(source=datasource, x='COUNTRY_FLYING_MISSION', color=Spectral3, width=0.7, stackers=['TONS_FRAG', 'TONS_IC', 'TONS_HE'], legend=['قطعات', 'آتش زا', 'انفجار قوی'])

show(p)