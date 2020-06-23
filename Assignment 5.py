# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:05:36 2020

@author: mstub
"""


# Assignment 5

import pandas as pd

### 1) Read and curate data

# Read in csv file
YT = pd.read_csv("yellow_tripdata_2017-06.csv") 

# Display data to only two decimals
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Converting pickup/drop-off times to datetime format
YT['pickup'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                              infer_datetime_format=True)

del YT['tpep_pickup_datetime'] #remove tpep pickup

YT['dropoff'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YT['tpep_dropoff_datetime'] #remove tpep drop off

# Calculate trip duration
YT['duration'] = YT['dropoff'] - YT['pickup']

# Deleting rows ("observations") that we don't want/need

# Delete trips < 100 miles
YT['valid'] = YT['trip_distance'] <= 100
YT = YT[YT.valid == True]

# delete trip distance = 0
YT['valid'] = YT['trip_distance'] != 0
YT = YT[YT.valid == True]

# delete any rows where passengers = 0 
YT['valid'] = YT['passenger_count'] > 0
YT = YT[YT.valid == True]

# fare amount make less than 1,000
YT['valid'] = YT['fare_amount'] < 1000 
YT = YT[YT.valid == True]

# fare amount make greater than zero
YT['valid'] = YT['fare_amount'] > 0 
YT = YT[YT.valid == True]

# make "extra" >= 0
YT['valid'] = YT['extra'] > 0 
YT = YT[YT.valid == True]

del YT['valid'] #remove validation column for next step

### 2) Provide descriptive data on the remaining observations.
print(YT[['trip_distance','passenger_count','duration',
          'fare_amount']].describe())
print(YT[['extra','mta_tax','tolls_amount',
          'improvement_surcharge','total_amount']].describe())


### 3) Save the curated data to a file called "YT_curated.csv"

YT.to_csv('YT_curated.csv', index = False)
