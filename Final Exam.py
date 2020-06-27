# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:05:54 2020

@author: mstub
"""

# Marc Stubel - Final Exam

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Read COVID data from .csv file
covid = pd.read_csv("us-states.csv")

# Explore data, sort, and find unique state names
covid
covid.dtypes
covid = covid.sort_values(by='state')
covid.state.unique()

# Delete data for states other than Pennsylvania
covid = covid[covid.state == 'Pennsylvania']

# Add formatted date column, sort, and delete original date column
covid['fdate'] = pd.to_datetime(covid['date'], infer_datetime_format=True)
covid = covid.sort_values(by='fdate')
del covid['date'] 

# Create new column called adj_deaths
covid['adj_deaths'] = covid['deaths']

# April 21st, 2020 deaths should be adjusted downward by 282
covid.loc[covid.fdate == '2020-04-21', 'deaths'] -= 282

# April 22nd, 2020 deaths should be adjusted downward by 297
covid.loc[covid.fdate == '2020-04-22', 'deaths'] -= 297

# Create a bar plot showing adj_deaths on the y-axis and dates on the x-axis.

plt.bar(covid.fdate, covid.adj_deaths, align='center', color='darkblue')
plt.grid(axis='y', alpha=0.25)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
plt.ylabel('Adjusted Deaths',fontsize=11)
plt.xlabel('Date',fontsize=11)
plt.xticks(fontsize=8) 
plt.yticks(fontsize=8) 
plt.title('PA Coronavirus Cumulative Deaths', fontsize=15)
plt.gcf().autofmt_xdate()
plt.show()