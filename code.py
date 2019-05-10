# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data = pd.DataFrame(data)
#Code starts here
data = data.rename(columns = {'Total': 'Total_Medals'})

print(type(data))
data.head(10)


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

#np.where(data['Total_Summer'] != data['Total_Winter'] , 'Both', 'NaN')))
#data['Better_Event'] = np.where(data['Total_Summer'] != data['Total_Winter'] , #)
print(type(data['Better_Event']))
better_event = data['Better_Event'].value_counts().index.values[0]
better_event


# --------------
#Code starts here
top_countries = data.loc[:, ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = pd.DataFrame(top_countries)
#top_countries.drop()
top_countries.tail()
top_countries.drop(top_countries.index[146], inplace = True)
#df.drop(df.index[0], inplace=True)
#def top_ten(top_countries ,column_name):
#    country_list = []
def top_ten(top_countries , column_name):
    country_list = []
    top_10 = top_countries.nlargest(10, column_name)
    
    country_list = list(top_countries.nlargest(10, column_name)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries ,'Total_Summer')
top_10_winter = top_ten(top_countries ,'Total_Winter')
top_10 = top_ten(top_countries ,'Total_Medals')

common = list( set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
summer_df = pd.DataFrame(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
winter_df = pd.DataFrame(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
top_df = pd.DataFrame(top_df)
print(type(summer_df))
summer_df.plot.bar(rot =0)
#w = winter_df.plot(bar)
#t = top_df.plot(bar)


# --------------
#Code starts here

summer_df['Golden_Ratio'] =  round(summer_df['Gold_Summer'] / summer_df['Total_Summer'], 2 )
summer_max_ratio  = summer_df['Golden_Ratio'].max()

a = (summer_df.loc[summer_df['Golden_Ratio'].idxmax()])
summer_country_gold = a['Country_Name']



winter_df['Golden_Ratio'] =  winter_df['Gold_Winter']  / winter_df['Total_Winter']
w= winter_df.loc[winter_df['Golden_Ratio'].idxmax()]
winter_country_gold = w['Country_Name']
winter_max_ratio = winter_df['Golden_Ratio'].max()

top_df['Golden_Ratio'] = round(top_df['Gold_Total']/ top_df['Total_Medals'], 2) 
top_max_ratio = top_df['Golden_Ratio'].max()
t = (top_df.loc[top_df['Golden_Ratio'].idxmax()])
top_country_gold = t['Country_Name']


# --------------
#Code starts here
data_1=data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
#most_points = data_1['Country_Name'].max()

#b = data_1.loc[data_1['Total_Points'].idxmax()]
#best_country = b['Country_Name']
#best_country


most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']




# --------------
#Code starts here
#best = pd.DataFrame(data , columns = 'Country_Name')
best = data[data['Country_Name'] == best_country]
(best) 
#best.iloc[:,13:16]
best = best[['Gold_Total','Silver_Total','Bronze_Total']].copy()
best.plot.bar(stacked =  False)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)





