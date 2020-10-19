import pandas as pd
from pandas import DataFrame

final = []
df = pd.read_excel(r'C:\Users\Amgh\PycharmProjects\eskandari\persian_date.xlsx', usecols=[1])
date = df.values.tolist()
print(date)
flat_date = []
for sublist in date:
    for item in sublist:
        flat_date.append(item)
cleanedList = [x for x in flat_date if str(x) != 'nan']
for date in cleanedList:
    Sp_date = date.split('-')
    if len(Sp_date[2]) == 1:
        Sp_date[2] = '0'+Sp_date[2]
    if len(Sp_date[1]) == 1:
        Sp_date[1] = '0'+Sp_date[1]
    final.append(Sp_date[0]+'/'+Sp_date[1]+'/'+Sp_date[2])

df_final = DataFrame (final,columns=['date'])

df_final.to_excel("states.xlsx")