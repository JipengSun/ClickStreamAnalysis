import pandas as pd
import csv

DATAPATH = '/Users/mac/PycharmProjects/ClickAnalysis'

#with open(DATAPATH+'/')

all_df = pd.read_csv(DATAPATH+'/clickstreamweek1-4.csv')
print(all_df.index)
dayslice = ['24/07/2017','25/07/2017','26/07/2017','27/07/2017','28/07/2017','29/07/2017','30/07/2017','31/07/2017','1/08/2017 ','2/08/2017 ','3/08/2017 ','4/08/2017 ','5/08/2017 ',
'6/08/2017 ', '7/08/2017 ','8/08/2017 ','9/08/2017 ','10/08/2017','11/08/2017','12/08/2017','13/08/2017','14/08/2017','15/08/2017','16/08/2017','17/08/2017','18/08/2017']

for index in all_df.index:
    for i in range(0,len(dayslice)):
        if all_df.loc[index]['timestamp'][0:10] == dayslice[i]:
            csvFile = open( str(i) +'.csv', 'a', newline='')  # 设置newline，否则两行之间会空一行
            writer = csv.writer(csvFile)
            data = all_df.loc[index].values
            print(data)
            writer.writerow(data)
            csvFile.close()
            #time.append(all_df.loc[index]['timestamp'][0:10])
            #print(all_df.loc[index]['timestamp'][0:10])
#print(time)














