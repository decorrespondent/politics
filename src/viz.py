# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import config
# import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
import fragmentatie

path_temp = config.PATH_TEMP_DATA
path_visuals = config.PATH_VIZ
path_source_data = config.PATH_SOURCE_DATA
path_output_data = config.PATH_OUTPUT_DATA

#viz (offline)
party_count = party_count.reset_index()
trace = go.Scatter(
        x = party_count['election_year'],
        y = party_count['total_parties'],
        
        )

data1 = [trace]
plot(data1)

# have the established parties become smaller? 
#TO DO: ONLY LOOK AT SOME OLD PARTIES 
viz_parties = df2.reset_index()
trace1 = go.Scatter(
        x = viz_parties['election_year'],
        y = viz_parties['vote_share'],
data2 = [trace1]
plot(data2)

