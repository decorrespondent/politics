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
len(elections)

# remove ep elections
elections = elections[elections['election_type'] == 'parliament']
len(elections)

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
                       'election_year']]

# merge with party info to get party family names
party = pd.read_csv(path_source_data + 'view_party.csv')
party = party[['party_id', 'family_id', 'family_name', 'left_right',
               'liberty_authority', 'eu_anti_pro']]
df = pd.merge(elections, party, on='party_id', how='left')
df = df.drop_duplicates()
len(df)

# remove non_eu members
non_eu_members = ['Norway', 'Canada', 'Australia', 'Switzerland',
                  'New Zealand', 'Iceland', 'Japan', 'Israel', 'Turkey']

df = df[~df['country_name'].isin(non_eu_members)]

# drop the UK and France because they are less proportional
disproportional = ['United Kingdom', 'France']

df = df[~df['country_name'].isin(non_eu_members)]

# since 1945
df = df[(df['election_year'] > 1945)]

# drop the rows that have no seats
df = df[df['party_name'] != 'no seat']

# only look at the netherlands

# make a series where party's are grouped by election year and see their vote share per election
def country_selector(country):
    df_country = df.loc[df['country_name'] == country]
    return df_country


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
    for year in range(min(df_country['election_year']),2019):
        if year in df_country['election_year'].unique():
            old_df_country = df_country.loc[df_country['election_year'] == year]
        else:
            old_df_country['election_year'] = year
            df_year = df_year.append(old_df_country)   

# sort df_year
df_year = df_year.sort_values(by=['country_name','election_year'])

# count the amount of parties in all EU-memberstates per year based on vote_share
party_count_EU_t = df_year.groupby('election_year').count()
party_count_EU = df_year.groupby(['country_name','election_year'])['vote_share'].count()
party_count_EU = pd.DataFrame(data=party_count_EU).rename(columns={'vote_share': 'total_parties'})

# count te amount of parties in all EU-memberstates per year based on seats
party_count_EU_seats = df_year.groupby(['country_name','election_year'])['vote_share'].count()
party_count_EU_seats = pd.DataFrame(data=party_count_EU).rename(columns={'vote_share': 'total_parties'})

# average amount of parties per year
parties_EU_mean = party_count_EU.groupby('election_year')['total_parties'].mean()

# has the vote_share of fammilies decreased
fam_EU = df_year.groupby(['election_year', 'family_name'])['vote_share'].mean()

# to csv
# df_year.to_csv(path_visuals + 'df_year.csv')
# party_count_EU.to_csv(path_visuals + 'party_count_EU.csv')
# fam_EU.to_csv(path_visuals + 'fam_eu.csv')

# biggest party nl for plotting in viz.py
nl = country_selector('Netherlands')
biggest_nl = nl.groupby('election_year')['vote_share'].max()

biggest_eu = df.groupby(['country_name', 'election_year'])['vote_share'].max()


# for all the countries in the EU
# for country in df_year['country_name'].unique():
#     (country).groupby(['election_year', 'party_name'])['vote_share'].mean()
    
 
   
# check the average of the last 10 years per country
    



# electoral volatility: the sum of th aggregated growth of all winning parties
# in comparison with the former election. 



        



# df2.groupby(['election_year', 'family_name'])['vote_share'].sum()

      
     

     
# interessting to see the sum of the diffrent columns in rows: df_year.groupby(['country_name', 'election_year' ]).aggregate(np.sum)     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    



