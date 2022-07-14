from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor4-resample.html')

data = pd.read_csv('thor_wwii.csv')
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'], format='%m/%d/%Y')

dataGrouped = data.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE'].sum()
datasource = ColumnDataSource(dataGrouped)

p = figure(x_axis_type='datetime')

p.line(source=datasource, x='MSNDATE', y='TOTAL_TONS', color='green', legend='جمع انفجارها', line_width=2)
p.line(source=datasource, x='MSNDATE', y='TONS_FRAG', color='blue', legend='قطعات', line_width=2)
p.line(source=datasource, x='MSNDATE', y='TONS_IC', color='red', legend='اتش زا', line_width=2)

show(p)