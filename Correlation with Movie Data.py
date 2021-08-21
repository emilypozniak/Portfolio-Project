#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)


#Import File

df = pd.read_csv(r'/Users/emilypozniak/Desktop/movies.csv')



#Previewing the data

df.head()



#Determining how much missing data there is

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, pct_missing))



#Determining the different types of data

df.dtypes




#Sorting the data by Gross Revenue

df.sort_values(by = ['gross'], inplace = False, ascending = False)




pd.set_option('display.max_rows', None)




#Trying to determine whether there is a correlation between Budget and Gross Revenue using a scatter plot

plt.scatter(x = df['budget'], y = df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget for Movie')
plt.ylabel('Gross Earnings')
plt.show()



#Adding a line to the scatter plot

sns.regplot(x = 'budget', y = 'gross', data = df, scatter_kws = {'color': 'red'}, line_kws = {'color': 'blue'})




#Creating a correlation matrix to determine which categories are highly correlated

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot= True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()



#Changing everything to a numeral so the correlation matrix can include all categories

df_numeric = df.copy(deep = True)

for col_name in df_numeric.columns:
    if(df_numeric[col_name].dtype == 'object'):
        df_numeric[col_name] = df_numeric[col_name].astype('category')
        df_numeric[col_name] = df_numeric[col_name].cat.codes
df_numeric.head()




correlation_matrix = df_numeric.corr()
sns.heatmap(correlation_matrix, annot= True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()




correlation_mat = df_numeric.corr()

corr_pairs = correlation_mat.unstack()

corr_pairs




#Pairing everything up

sorted_pairs = corr_pairs.sort_values()
sorted_pairs




#Finding the highest correlated pairs

high_corr = sorted_pairs[(sorted_pairs)> 0.5]
high_corr




#Votes and budget have the highest correlation to gross revenue.

