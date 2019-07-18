# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import config
import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
import fragmentatie
import matplotlib.pyplot as plt
import seaborn as sns

path_temp = config.PATH_TEMP_DATA
path_visuals = config.PATH_VIZ
path_source_data = config.PATH_SOURCE_DATA
path_output_data = config.PATH_OUTPUT_DATA

# viz (offline)
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

# amount of parties in the EU viz:
parties_EU_mean = pd.DataFrame(parties_EU_mean.reset_index())
trace = go.Scatter(
        x = parties_EU_mean['election_year'],
        y = parties_EU_mean['total_parties'])
data = [trace]
plot(data)
py.image.save_as(data, path_visuals + 'parties_EU_mean.png')

#plot the biggest
plt.plot(biggest_nl)

sns.set(style="ticks")

# plot the parties of the EU-countries using seaborn
party_count_EU = party_count_EU.reset_index()
g = sns.FacetGrid(party_data, col='country_name', col_wrap = 4)
g.map(plt.scatter,'election_year','total_parties')

g = sns.FacetGrid(party_data, col='country_name', col_wrap = 4)
g.map(sns.pointplot,'election_year', 'total_parties', color=".3", ci=None)

g = sns.FacetGrid(party_count_EU, col='country_name', col_wrap = 4)
g.map(sns.lineplot,'election_year', 'total_parties',color=".3")
g.map(plt.axhline, y=13, color='k', linestyle=":")
g.map(sns.lineplot,
      x = parties_EU_mean['election_year'],
      y = parties_EU_mean['total_parties'],
      linestyle = ":")
g.savefig('EU_parties.pdf')

#put the mean as a line that goes through them
g = sns.FacetGrid(tips, col="time")






