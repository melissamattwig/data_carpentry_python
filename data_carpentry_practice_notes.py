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



#subsetting data!!!
#two ways to subset data,
#1 use brackets
survey_df['species_id']
#2 use the name of the column you want as an attribute, like so:
survey_df.species_id
#can look at multiple columns at once
survey_df[['species_id', 'plot_id']]
#create as a new object to work with
survey_species = survey_df['species_id']

#reminder from datacarpentry: DO NOT USE reserved words, list is online

#slicing
#select row, row 3 IS NOT SELECTED
surves_df[0:3]
#select first 5 rows (0, 1, 2, 3, 4)
survey_df[:5]
#select last element
survey_df[-1:]

#BE CAREFUL of referencing using the = sign vs. copying .copy()

#slicing subsets
# iloc[row slicing, column slicing]
survey_df.iloc[0:3, 1:4]
# Select all columns for rows of index values 0 and 10
survey_df.loc[[0, 10], :]
# Syntax for iloc indexing to finding a specific data element
dat.iloc[row, column]
#row 2 of column 6
survey_df.iloc[2, 6]
#slices rows 0 through 3 and its 2nd through 5th column
survey_df.iloc[0:4, 1:4]
#look at all rows that have 2002 values
survey_df[survey_df.year == 2002]
#all rows that DO NOT CONTAIN 2002
survey_df[survey_df.year != 2002]
#set of criteria, for example rows with years greater than 1980 but 1985 or less
survey_df[(survey_df.year >= 1980) & (survey_df.year <= 1985)]
#challenge: select subset with data from the year 1999 and that
#contains weight values less than or equal to 8
survey_df[(survey_df.year == 1999) & (survey_df['weight'] <= 8)]
#yay!
#second part of the challenge asks to use ~ to show M or F, but I did it more directly
survey_df[survey_df['sex'].isin(['F'])]

#BOOLEAN i.e true/false
#show all null spots in dataframe
pd.isnull(survey_df)
#select null value rows, use mask as an index to subset
#use .any()
survey_df[pd.isnull(survey_df).any(axis=1)]
#what does this do?
empty_weights = survey_df[pd.isnull(survey_df['weight'])]['weight']
print(empty_weights)
#shows all rows that have NaN in the weight column by using boolean object

#challenge part one
#Create a new DataFrame that only contains observations with sex values that are not female or male.
#Assign each sex value in the new DataFrame to a new value of ‘x’.
#Determine the number of null values in the subset.
empty_sex = survey_df[pd.isnull(survey_df['sex'])]['sex']
copy_empty_sex = empty_sex.copy()
copy_empty_sex.fillna(value='x', inplace = True)
copy_empty_sex.count()
#output 2511

#challenge part two
#Create a new DataFrame that contains only observations that are of sex male or female
#and where weight values are greater than 0. Create a stacked bar plot of average
#weight by plot with male vs female values stacked for each plot.
copy_survey_df = survey_df.copy()
copy_survey_df = copy_survey_df.dropna()
copy_survey_df[(copy_survey_df['weight'] >= 0)]
site_sex = copy_survey_df.groupby(['plot_id', 'sex'])
site_sex_count = site_sex['weight'].sum()
pc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")

#checking format types
survey_df['sex'].dtype
#output is O for object
survey_df['record_id'].dtype
#output is int64
#data type for each column
survey_df.dtypes
#convert float to integer using int()
#convert integer to float using float()
#convert the record_id field from an integer to a float
survey_df['record_id'] = survey_df['record_id'].astype('float64')

#write out NaN data and save copy as csv to use later
#FULL path from the beginning
import pandas as pd
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv")
copy_survey_df = survey_df.copy()
copy_survey_df = copy_survey_df.dropna()
copy_survey_df.to_csv('C:\Coding\data_carpentry_python-master\data\surveys_complete.csv', index=False)


#Combining datdaframes!!!
import pandas as pd
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv", keep_default_na=False, na_values=[""])
species_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\species.csv",
                         keep_default_na=False, na_values=[""])

#read first 10 lines of surveys table
survey_sub = survey_df.head(10)
#read last 10 rows
survey_sub_last10 = survey_df.tail(10)
#reset the index values to the second dataframe
#drop=True option avoids adding new index column with old index values
survey_sub_last10 = survey_sub_last10.reset_index(drop=True)

#stack the dataframes on top of each other
vertical_stack = pd.concat([survey_sub, survey_sub_last10], axis=0)
print(vertical_stack)
#dataframes side by side
horizontal_stack = pd.concat([survey_sub, survey_sub_last10], axis=1)
print(horizontal_stack)
#write vertical_stack to csv file
vertical_stack.to_csv('C:\Coding\data_carpentry_python-master\data\out.csv', index=False)

#challenge: In the data folder, there are two survey data files: survey2001.csv and survey2002.csv.
#Read the data into Python and combine the files to make one new data frame.
#Create a plot of average plot weight by year grouped by sex
#Export your results as a CSV and make sure it reads back into Python properly.
#but that data doesn't exists in the provided data, so I could just slice out data by year

#So we can combine dataframes by using a query so we can keep dataframe sizes optimal

import pandas as pd
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv", keep_default_na=False, na_values=[""])
#using first 10 rows for ease of small dataframe
survey_sub = survey_df.head(10)
species_sub = pd.read_csv('C:\Coding\data_carpentry_python-master\data\species.csv', keep_default_na=False, na_values=[""])
#speciesSubset doesn't exist in provided data

#look at columns of both dataframes so as to find one to be the join key
species_sub.columns
survey_sub.columns
#species_id is on both
#could leave left on and right on blank since there's only one join key
merged_inner = pd.merge(left=survey_sub, right=species_sub, left_on='species_id', right_on='species_id')
#merge from the left
merged_left = pd.merge(left=survey_sub, right=species_sub, how='left', left_on='species_id', right_on='species_id')
merged_left
#on the website it shows that the inner merge should be different from the left merge
#in terms of how many rows are included, but I didn't see that???

#challenge: Create a new DataFrame by joining the contents of the surveys.csv and species.csv tables
#Then calculate and plot the distribution of: 1) taxa by plot and, 2) taxa by sex by plot

import pandas as pd
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv", keep_default_na=False, na_values=[""])
species_df = pd.read_csv('C:\Coding\data_carpentry_python-master\data\species.csv', keep_default_na=False, na_values=[""])
copy_survey_df = survey_df.copy()
merged_left = pd.merge(left=survey_df,right=species_df, how='left', on="species_id")
#the bar plot looks weird
merged_left.groupby(["plot_id"])["taxa"].nunique().plot(kind='bar')

#by taxa by sex by plot
merged_left.loc[merged_left["sex"].isnull(), "sex"] = 'M|F'

#they add things that they didn't talk about like the M|F thing...

ntaxa_sex_site= merged_left.groupby(["plot_id", "sex"])["taxa"].nunique().reset_index(level=1)
ntaxa_sex_plot = ntaxa_sex_site.pivot_table(values="taxa", columns="sex", index=ntaxa_sex_site.index)
ntaxa_sex_site.plot(kind="bar", legend=Fa

#Challenge 2: Calculate a diversity index of your choice for control vs rodent exclosure plots.
#The index should consider both species abundance and number of species.
#You might choose to use the simple biodiversity index described here which calculates diversity as:
#the number of species in the plot / the total number of individuals in the plot

import pandas as pd
survey_df = pd.read_csv("C:\Coding\data_carpentry_python-master\data\surveys.csv", keep_default_na=False, na_values=[""])
species_df = pd.read_csv('C:\Coding\data_carpentry_python-master\data\species.csv', keep_default_na=False, na_values=[""])
merged_left = pd.merge(left=survey_df,right=species_df, how='left', on="species_id")
# number of species per site
nspecies_site = merged_left.groupby(["plot_id"])["species_id"].nunique().rename("nspecies")
# number of individuals per site
nindividuals_site = merged_left.groupby(["plot_id"]).count()['record_id'].rename("nindiv")
#combine them
diversity_index = pd.concat([nspecies_site, nindividuals_site], axis=1)
#calculate diversity index
diversity_index['diversity'] = diversity_index['nspecies']/diversity_index['nindiv']
diversity_index['diversity'].plot(kind="barh")

