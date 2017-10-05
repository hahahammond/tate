# Import modules
import pandas as pd
import urllib3
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import re

# Read in csv file from Tate's GitHub
tate = pd.read_csv("https://raw.githubusercontent.com/tategallery/collection/master/artist_data.csv")

# Fix the 'yearOfBirth' column so they NaNs are filled and they are integers
tate['yearOfBirth'] = tate['yearOfBirth'].fillna(0).astype(int)

# Explore tate df
print(tate.head())
print(tate.describe())
print(tate.dtypes)

# Create counts_by_gender df with groupby
counts_by_gender = tate.groupby(['gender']).id.count()
print(counts_by_gender)

# Plot counts_by_gender df
counts_by_gender.plot(kind='bar', stacked=True)





### ARTISTS BORN AFTER 1500  ###

# Create sixteenth_cent by subsetting for artists born after 1500
sixteenth_cent = tate.loc[tate['yearOfBirth'] >= 1500]

# Explore twentieth_cent df
print(sixteenth_cent.head())
print(sixteenth_cent['yearOfBirth'].max())
print(sixteenth_cent['yearOfBirth'].min())
print(sixteenth_cent.loc[sixteenth_cent['yearOfBirth'] == 1775])

# Create counts by birth year and gender df with groupby
sixteenth_cent_counts = sixteenth_cent.groupby(['gender', 'yearOfBirth']).id.count().unstack().transpose().fillna(0)

# Fix gender counts so they are integers
sixteenth_cent_counts.Female = sixteenth_cent_counts.Female.astype(int)
sixteenth_cent_counts.Male = sixteenth_cent_counts.Male.astype(int)

# Explore df
sixteenth_cent_counts.head()
sixteenth_cent_counts.describe()
sixteenth_cent_counts.dtypes

# Plot df
sixteenth_cent_counts.plot(kind='bar', stacked=True)
sixteenth_cent_counts.plot(kind='line')






### ARTISTS BORN AFTER 1900 ###

# Create twentieth_cent by subsetting for artists born after 1900
twentieth_cent = tate.loc[tate['yearOfBirth'] >= 1900]

# Explore df
print(twentieth_cent.head())
print(twentieth_cent['yearOfBirth'].max())
print(twentieth_cent['yearOfBirth'].min())
print(twentieth_cent.loc[twentieth_cent['yearOfBirth'] == 1945])

# Create counts by birth year and gender df with groupby
twentieth_cent_counts = twentieth_cent.groupby(['gender', 'yearOfBirth']).id.count().unstack().transpose().fillna(0)

# Fix gender counts so they are integers
twentieth_cent_counts.Female = twentieth_cent_counts.Female.astype(int)
twentieth_cent_counts.Male = twentieth_cent_counts.Male.astype(int)

# Explore df
twentieth_cent_counts.head()
twentieth_cent_counts.describe()
twentieth_cent_counts.dtypes

# Plot df
twentieth_cent_counts.plot(kind='bar', stacked=True)
twentieth_cent_counts.plot(kind='line')





### ARTIST WHO ARE GENERATION X  ###

# Create gen_x by subsetting for artists born after 1970
gen_x = tate[(tate['yearOfBirth'] >= 1965) & (tate['yearOfBirth'] <= 1984)]

# Explore df
print(gen_x.head())
print(gen_x['yearOfBirth'].max())
print(gen_x['yearOfBirth'].min())
print(gen_x.loc[gen_x['yearOfBirth'] == 1980])

# Create counts by birth year and gender df with groupby
gen_x_counts = gen_x.groupby(['gender', 'yearOfBirth']).id.count().unstack().transpose().fillna(0)

# Fix gender counts so they are integers
gen_x_counts.Female = gen_x_counts.Female.astype(int)
gen_x_counts.Male = gen_x_counts.Male.astype(int)

# Explore df
gen_x_counts.head()
gen_x_counts.describe()
gen_x_counts.dtypes

# Plot df
gen_x_counts.plot(kind='bar', stacked=True)
gen_x_counts.plot(kind='line')


# Create dataframe of artists born in the USA
americans = pd.DataFrame(columns=tate.columns)

for item, frame in tate['placeOfBirth'].iteritems():
    match = re.search("United States", str(frame))
    if match:
        #print(tate.loc[item])
        americans = americans.append(tate.loc[item],ignore_index=True)

print(americans.info())
        
        
# Create dataframe of artists born in Boston

bostonians = pd.DataFrame(columns=tate.columns)

for item, frame in tate['placeOfBirth'].iteritems():
    match = re.search("Boston", str(frame))
    if match:
        #print(tate.loc[item])
        bostonians = bostonians.append(tate.loc[item],ignore_index=True)

print(bostonians.info())



