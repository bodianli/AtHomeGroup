# 1. After using SSIS to present basic ETL process, I got transformed dataset data from difference sources.
# 2. Load Simulated and transformed Data to SQL Server and conduct further data transformation
# 3. Query can be found from  "SQL_Transform", and I posted transformed details and saved it as Store Procedure in SSMS
# 4. "eda_2.csv" is final dataset for current project


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("eda_2.csv", encoding="UTF-8")


# The dataset can be splited into three parts: Trend_Data, 2020_Update_statistic Data, Simulated_Sales
# Trend_Data: According to the offical website,as there is no statistical result for the latest 2020 data so far, which means that the trend data we can collect is for the 9 period from 2010-2019
# https://www.census.gov/acs/www/data/data-tables-and-tools/data-profiles/2019/
# 2020_Update_statistic_data: Although there is no Trend_data for 2020, but we can find demographic, Race_Ethic, ACS


# Simple_exponential_smoothing
def exponential_smoothing(series, alpha):
    """
        series - dataset with timestamps
        alpha - float [0.0, 1.0], smoothing parameter
    """
    result = [(series[0] + series[1] + series[2]) / 3]  # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])
    return result[len(series) - 1]


# Double_exponential_smoothing
def double_exponential_smoothing(series, alpha, beta):
    """
        series - dataset with timeseries
        alpha - float [0.0, 1.0], smoothing parameter for level
        beta - float [0.0, 1.0], smoothing parameter for trend
    """
    # first value is same as series
    result = [series[0]]
    for n in range(1, len(series) + 1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series):  # forecasting
            value = result[-1]
        else:
            value = series[n]
        last_level, level = level, alpha * value + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        result.append(level + trend)
    return result[len(series) - 1]


column_list = data.columns.values.tolist()

# Split List Name to 15 chunk for predicting 2020 trend
POPESTIMATE = column_list[31:41]
NPOPCHG = column_list[41:51]
BIRTHS = column_list[51:61]
DEATHS = column_list[61:71]
NATURALINC = column_list[71:81]
INTERNATIONALMIG = column_list[81:91]
DOMESTICMIG = column_list[91:101]
NETMIG = column_list[101:111]
RESIDUAL = column_list[111:121]
GQESTIMATES = column_list[122:132]
RBIRTH = column_list[132:141]
RDEATH = column_list[141:150]
RNATURALINC = column_list[150:159]
RINTERNATIONALMIG = column_list[159:168]
RDOMESTICMIG = column_list[168:177]
RNETMIG = column_list[177:186]

#
# print(data[RESIDUAL].head())


# Test function by POPESTIMATE columns
print(data.loc[0, POPESTIMATE])
print(exponential_smoothing((data.loc[0, POPESTIMATE]), 0.5))
print(double_exponential_smoothing((data.loc[0, POPESTIMATE]), 0.5, 0.5))


# 2020 Feature for Simple_exponential_smoothing
data['NPOPCHG2020'] = data.loc[:, NPOPCHG].apply(exponential_smoothing, args=(0.5,), axis=1)
data['BIRTHS2020'] = data.loc[:, BIRTHS].apply(exponential_smoothing, args=(0.5,), axis=1)
data['DEATHS2020'] = data.loc[:, DEATHS].apply(exponential_smoothing, args=(0.5,), axis=1)
data['NATURALINC2020'] = data.loc[:, NATURALINC].apply(exponential_smoothing, args=(0.5,), axis=1)
data['NETMIG2020'] = data.loc[:, NETMIG].apply(exponential_smoothing, args=(0.5,), axis=1)
data['RESIDUAL2020'] = data.loc[:, RESIDUAL].apply(exponential_smoothing, args=(0.5,), axis=1)
data['RBIRTH2020'] = data.loc[:, RBIRTH].apply(exponential_smoothing, args=(0.5,), axis=1)
data['RDEATH2020'] = data.loc[:, RDEATH].apply(exponential_smoothing, args=(0.5,), axis=1)

# 2020 Feature for Double_exponential_smoothing
data['POPESTIMATE2020'] = data.loc[:, POPESTIMATE].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['INTERNATIONALMIG2020'] = data.loc[:, INTERNATIONALMIG].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['DOMESTICMIG2020'] = data.loc[:, DOMESTICMIG].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['GQESTIMATES2020'] = data.loc[:, GQESTIMATES].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['RNATURALINC2020'] = data.loc[:, RNATURALINC].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['RINTERNATIONALMIG2020'] = data.loc[:, RINTERNATIONALMIG].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['RDOMESTICMIG2020'] = data.loc[:, RDOMESTICMIG].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)
data['RNETMIG2020'] = data.loc[:, RNETMIG].apply(double_exponential_smoothing, args=(0.5,0.5,), axis=1)


data.to_csv("Simu_2010_2020_dataset.csv")





# print(data['POPESTIMATE2020'].head())

# print(data['POPESTIMATE2020'].head())
# print(data['ESTIMATESBASE2020'].head())
