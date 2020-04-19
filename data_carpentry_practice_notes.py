# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello World")
#python starts at 0
#dictionaries contain pairs of objects, a key and associated value
#rev is the dictionary
rev = {'first': 'one', 'second': 'two'}
rev['third'] = 'three'
#adds arrows in the dictionary
for key, value in rev.items():
    print(key, '->', value)
    
#add a function
def add_function(a, b):
    result = a + b
    return result
#associates z with the function I indicated
z = add_function(20, 22)
print(z)

#working with dataframes section of datacarpentry
#Pandas is a library good for working with tabular data
#import library as nickname pd
import pandas as pd
pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv")
#assign the dataframe to a variable
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv")
#see first few columns of dataframe
survey_df.head()
#dtypes shows what type of things we have in the dataframe
survey_df.dtypes
#different ways to look at attributes of the dataframe
survey_df.columns
#first 15 rows
survey_df.head(15)
#tells us the different things within the attribute we're looking at
pd.unique(survey_df['species_id'])
#how many variables in the plot_id
survey_df['plot_id'].nunique()
#basic stats
survey_df['weight'].describe()
#group data by specific group, in this case sex, in order to run stats
#Tis powerful b/c it allows us to quickly generate summary stats.
grouped_data = survey_df.groupby('sex')
grouped_data.describe()

#challenge, observe what happens for the following:
grouped_data2 = survey_df.groupby(['plot_id', 'sex'])
grouped_data2.mean()
#grouped by sex and plot_id   
#Summarize weight values for each site in your data using by_site['weight'].describe()
#this creates summary stats for only one column
by_site = survey_df.groupby(['plot_id'])
by_site['weight'].describe()

#group by how many animals in each species
species_counts = survey_df.groupby('species_id')['record_id'].count()
print(species_counts)
#or specifically by 1 species, DO in this case
survey_df.groupby('species_id')['record_id'].count()['DO'] 

%matplotlib inline
#bar chart
species_counts.plot(kind='bar');          

#plot how many animals in each plot
total_count = survey_df.groupby('plot_id')['record_id'].nunique()
total_count.plot(kind='bar');

#challenge
#1 Create a plot of average weight across all species per site.
avg_weight = survey_df.groupby('plot_id')['weight'].mean()
avg_weight.plot(kind='bar');

#2 Create a plot of total males versus total females for the entire dataset.
sex_counts = survey_df.groupby('sex')['record_id'].count()
sex_counts.plot(kind='bar');

#summary challenge: Create a stacked bar plot, with weight on the Y axis and the
#stacked variable being sex. The plot should show total weight by sex for each site
#group by site and sex
site_sex = survey_df.groupby(['plot_id', 'sex'])
#calculate total weight for each site
site_sex_count = site_sex['weight'].sum()
#.unstack() shows how much weight by sex in each site
site_sex_count.unstack()
spc = site_sex_count.unstack()

#bar plot where each weights for each sex are stacked by site
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
#set label names
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")