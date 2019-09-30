import pandas as pd
import datetime
import config
# import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt

path_temp = config.PATH_TEMP_DATA
path_visuals = config.PATH_VIZ
path_source_data = config.PATH_SOURCE_DATA
path_output_data = config.PATH_OUTPUT_DATA


# get a all elections
elections = pd.read_csv(path_source_data + 'view_election.csv')

# remove ep elections
elections = elections[elections['election_type'] == 'parliament']

# extract election year
elections['election_year'] = pd.to_datetime(elections['election_date']).dt.year

# select necessary columns
elections = elections[['country_name',
                       'country_name_short',
                       'vote_share',
                       'seats',
                       'party_id',
                       'party_name',
                       'party_name_english',
                       'election_year',
                       'election_id']]

# merge with party info to get party family names
party = pd.read_csv(path_source_data + 'view_party.csv')
party = party[['party_id', 'family_id', 'family_name', 'left_right',
               'liberty_authority', 'eu_anti_pro']]
df = pd.merge(elections, party, on='party_id', how='left')
df = df.drop_duplicates()

# merge with calculations election paramaters to get the calculated values done by parlgov
parameters = pd.read_csv(path_source_data + 'viewcalc_election_parameter.csv')
df = pd.merge(df, parameters, on='election_id', how='left')


# remove non_eu members
non_eu_members = ['Norway', 'Canada', 'Australia', 'Switzerland',
                  'New Zealand', 'Iceland', 'Japan', 'Israel', 'Turkey']

df = df[~df['country_name'].isin(non_eu_members)]

# since 1945
df = df[(df['election_year'] > 1945)]

# drop the rows that have no seats
df = df[df['party_name'] != 'no seat']
df = df[df['party_name'] != 'one seat']

# only look at the netherlands

# make a series where party's are grouped by election year and see their vote share per election
def country_selector(country):
    df_country = df.loc[df['country_name'] == country]
    return df_country

df_country = country_selector('Netherlands')`


df2 = country_selector('Netherlands').groupby(
        ['election_year', 'party_name'])['vote_share'].mean()

# look at the individual countries.

# count the amount of parties per election in a new df based on voteshare
party_count = df2.groupby('election_year').count()
party_count = pd.DataFrame(data=party_count).rename(
        columns={'vote_share': 'total_parties'})

# turn the data into years HIER BEN IK NU BEZIG, DUS NIET AF.
# probeer
# df_63 = df[df['party_id'] == 63]
# for index, row in df_63.iterrows():
#     nextyear_df = df_63[df_63['election_year'] == row['election_year'] + 1]
#     if nextyear_df.empty:
#         new_row = row
#         new_row['election_year'] = row['election_year'] + 1
#         print(row['election_year'], new_row['election_year'])
#         df_63 = df_63.append(new_row)

df_year = df

for country in df['country_name'].unique():
    df_country = df.loc[df['country_name'] ==country]
    for year in range(min(df_country['election_year']),2020):
        if year in df_country['election_year'].unique():
            old_df_country = df_country.loc[df_country['election_year'] == year]
        else:
            old_df_country['election_year'] = year
            df_year = df_year.append(old_df_country)

# sort df_year
df_year = df_year.sort_values(by=['country_name','election_year'])

# count the amount of parties in all EU-memberstates per year based on vote_share
party_count_EU = df_year.groupby(['country_name','election_year'])['vote_share'].count()
party_count_EU = pd.DataFrame(data=party_count_EU).rename(columns={'vote_share': 'total_parties'})

# count te amount of parties in all EU-memberstates per year based on seats
df_year_seats = df_year[df_year['seats'] > 0]
party_count_EU_seats = df_year_seats.groupby(['country_name','election_year'])['seats'].count()
party_count_EU_seats = pd.DataFrame(data=party_count_EU_seats).rename(columns={'seats': 'total_parties_seats'})
# party_count_EU_seats.to_csv(path_visuals + 'party_count_EU_seats.csv')

# get the party counts in one table
party_count_EU['total_parties_seats'] = df_year_seats.groupby(['country_name','election_year'])['seats'].count()

# average amount of parties per year based on vote share
parties_EU_mean = party_count_EU.groupby('election_year')['total_parties'].mean()

# average amount of parties per year based on seats
parties_EU_seats_mean = party_count_EU_seats.groupby('election_year')['total_parties_seats'].mean()
parties_EU_seats_mean.to_csv(path_visuals + 'parties_EU_seats_mean.csv')

# has the vote_share of fammilies decreased
fam_EU = df_year.groupby(['election_year', 'family_name'])['vote_share'].mean()
fam_EU_seats = df_year.groupby(['election_year', 'family_name'])['seats'].mean()

# biggest party nl for plotting in viz.py
nl = country_selector('Netherlands')
biggest_nl = nl.groupby('election_year')['vote_share'].max()
biggest_eu = df.groupby(['country_name', 'election_year'])['vote_share'].max()

# calculate the mean of the enp_seats
enp_mean = df_year.groupby(['election_year'])['enp_seats'].mean()
enp_mean2 = df_year.groupby(['election_year','country_name'])['enp_seats'].mean()

# calculate the mean of the enp_votes
enp_mean_votes = df_year.groupby(['election_year'])['enp_votes'].mean()

# calculate the median of the enp_seats
enp_median = df_year.groupby(['election_year'])['enp_seats'].median()

# trying something removing one seats
nl = nl[nl['party_name'] != 'no seat']

# TO CSV
# df_year.to_csv(path_visuals + 'df_year.csv')
# df_year_seats.to_csv(path_visuals + 'df_year_seats.csv')
# party_count_EU.to_csv(path_visuals + 'party_count_EU.csv')
# fam_EU.to_csv(path_visuals + 'fam_eu.csv')
# fam_EU_seats.to_csv(path_visuals + 'fam_eu_seats.csv')
# party_count.to_csv(path_visuals + 'party_count_nl.csv')
enp_mean.to_csv(path_visuals + 'enp_mean.csv')






     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    



