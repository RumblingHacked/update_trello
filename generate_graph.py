import globals
import plotly.graph_objs as go
import plotly
from plotly.offline import plot

plotly.tools.set_credentials_file(username='RumblingHacked', api_key=globals.environ.get('PLOTLY_KEY'))

# Variables that we need for the graph
areacodes_completed = len(globals.list_completed.list_cards())
areacodes_in_progress = len(globals.list_in_progress.list_cards())
areacodes_left = len(globals.list_area_codes.list_cards())

# Generate graph
labels = ['Completed', 'In Progress', 'Not-Completed']
values = [areacodes_completed, areacodes_in_progress, areacodes_left]
colors = ['#EACF19', '#ffffff', '#1D0C23']

trace = go.Pie(labels= labels, values= values, hoverinfo='label+percent', textinfo='value', textfont=dict(size=20), marker=dict(colors=colors, line=dict(color='#000000', width=2)))

plot([trace], filename='area_code_progress.html')