import math
import csv
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

#European Union Allowance Price
def average(list):
    sum = 0
    for val in list:
        if not math.isnan(val):
            sum+=val
    return float(sum)/len(list)

#work here: create new csv file with the following indicators (all based on USD not EURO)
#price: mean, minimum, q1, q3, maximum prices of each year 
# create opaqued graph with each indicator
df = pd.read_csv("carbon stuff workbook - European Credit Prices (1).csv")
indices = [i for i in range(0, df.shape[0])]
df = df.assign(index = indices)
df.set_index('index', inplace=True)

num_lines = df.shape[0]
print("Number of lines in the CSV file: ", num_lines)

# calculating the new indicators for the new csv - 
needed_col = ['EUR_USD','NZ_USD', 'UK_USD', 'CHN_USD', 'WAS_USD']
years_list = [year for year in range(2005, 2024)]
dict= {'year':years_list,'EUR_USD':[],'NZ_USD':[], 'UK_USD':[], 'CHN_USD':[], 'WAS_USD':[]}

#every column
for c in range(0, len(needed_col)):
    indicator = dict[needed_col[c]]
    current_indx_yearlist = 0
    #list of all price data (in this ETS) from this years_list[current_indx_yearlist] year
    year_data = []
    for i in range(0, df.shape[0]):
        if df["Date"][i].find(str(years_list[current_indx_yearlist]))!= -1:
            #print(needed_col[c], i, df[needed_col[c]][i])
            year_data.append(df[needed_col[c]][i])
        else:
            #print(sum(year_data), max(year_data), len(year_data), average(year_data))
            indicator.append(average(year_data))
            current_indx_yearlist = current_indx_yearlist+1
            year_data = []
    indicator.append(sum(year_data)/len(year_data))

# for c in range(0, len(needed_col)):
#     indicator = dict[needed_col[c]]
#     print(len(indicator), len(years_list))
DF = pd.DataFrame(dict)
DF.to_csv('annual_mean_CO2_prices_by_ETS.csv')

