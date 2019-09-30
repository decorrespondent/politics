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

#for viz we need to reset the df's because of indexing
party_count = party_count.reset_index()
parties_EU_mean = pd.DataFrame(parties_EU_mean.reset_index())
parties_EU_seats_mean = parties_EU_seats_mean.reset_index()
enp_mean = enp_mean.reset_index()
enp_median = enp_median.reset_index()
enp_mean_votes = enp_mean_votes.reset_index()

# viz with plotly (offline)

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

trace = go.Scatter(
        x = parties_EU_mean['election_year'],
        y = parties_EU_mean['total_parties'])
data = [trace]
plot(data)
py.image.save_as(data, path_visuals + 'parties_EU_mean.png')

#plot the biggest
plt.plot(biggest_nl)

sns.set(style="ticks")

# plot the amount of parties of the EU-countries using seaborn (image if we have )
party_count_EU = party_count_EU.reset_index()
g = sns.FacetGrid(party_data, col='country_name', col_wrap = 4)
g.map(plt.scatter,'election_year','total_parties')

g = sns.FacetGrid(party_data, col='country_name', col_wrap = 4)
g.map(sns.pointplot,'election_year', 'total_parties', color=".3", ci=None)

grid = sns.FacetGrid(party_count_EU, col='country_name', col_wrap = 4)
grid.map(sns.lineplot,'election_year', 'total_parties',color=".3")
grid.map(plt.axhline, y=13, color='k', linestyle=":")

# map the EU_vote_share_mean
grid.map(sns.lineplot,
      x = parties_EU_mean['election_year'],
      y = parties_EU_mean['total_parties'],
      linestyle = ":")
grid.map(sns.lineplot, 'election_year', 'total_parties_seats', color = 'red')
grid.savefig('EU_parties_3.pdf')

# plot the parties of the EU-countries based on seats
party_count_EU_seats = party_count_EU_seats.reset_index()

grid = sns.FacetGrid(party_count_EU_seats, col='country_name', col_wrap = 4)
grid.map(sns.lineplot,'election_year', 'total_parties',color=".3")
# map the line with the dutch amount of parties last election (13)
grid.map(plt.axhline, y=13, color='k', linestyle=":")
# map the EU_seats_mean
grid.map(sns.lineplot,
         x = parties_EU_seats_mean['election_year'],
         y = parties_EU_seats_mean['total_parties'],
         linestyle = ":")
grid.savefig('EU_parties_seats.pdf')

# plot the enp_seats
grid = sns.FacetGrid(df_year_seats, col='country_name', col_wrap = 4)
grid.map(sns.lineplot,'election_year','enp_seats')
grid.map(sns.lineplot,
         x = enp_mean['election_year'],
         y = enp_mean['enp_seats'],
         color = '.3')

grid.savefig('enp_seats.pdf')

# single EU_ENP_seats_mean:
ax = sns.lineplot(x = 'election_year', y = 'enp_seats', data = enp_mean, color = '.3')

# single EU_ENP_votes_mean:
ax = sns.lineplot(x = 'election_year', y = 'enp_votes', data = enp_mean_votes, color = '.3')

# single EU_seats_median:
ax = sns.lineplot(x = 'election_year', y = 'enp_seats', data = enp_median, color = '.3')

