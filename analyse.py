# -*- coding: utf-8 -*-
# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rows =[]
f = open('filteredlist.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
finally:
    f.close()

df = pd.read_csv('filteredlist.csv' , names=['id', 'word', 'tagType', 'sentencenumber'])

personCount , locationCount , organizationCount, productCount= 0,0,0,0
dateCount , moneyCount , percentCount ,otherCount= 0,0,0,0



for i in range(0, len(df) - 1):
    if df.tagType[i] == 'Person':
        personCount += 1
    elif df.tagType[i] == 'Location':
        locationCount += 1
    elif df.tagType[i] == 'Organization':
        organizationCount += 1
    elif df.tagType[i] == 'Product':
        productCount += 1
    elif df.tagType[i] == 'Date':
        dateCount += 1
    elif df.tagType[i] == 'Money':
        moneyCount += 1
    elif df.tagType[i] == 'Percent':
        percentCount += 1
    else:
        otherCount += 1

tagTypes = ['Person' , 'Location' , 'Organization' , 'Product' , 'Date' , 'Money' , 'Percent']


counter = [personCount, locationCount,organizationCount, productCount,dateCount, moneyCount,percentCount]
list = {'tagTypes':tagTypes,'counter': counter}
df_taglist =pd.DataFrame(list)

print df_taglist

print "***Max value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== max(df_taglist.counter)].index]

print "\n***Min value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== min(df_taglist.counter)].index]

print "\n***Mean of tagged word:",df_taglist.mean()

print "\n***Standart deviation of tagged word:",df_taglist.std()


N=7
## necessary variables
ind = np.arange(N)  # the x locations for the groups
width = 0.25  # the width of the bars
menStd = [0, 0, 0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot(111)
rects4 = ax.bar(ind, counter, width,color='black',yerr=menStd, error_kw=dict(elinewidth=7, ecolor='red'))

# axes and labels
ax.set_xlim(-width, len(ind) + width)
ax.set_ylim(0, max(df_taglist.counter)+100)
ax.set_title('class histogram')
xTickMarks = ['person','location','organization', 'product','date','money','percent']
ax.set_xticks(ind + width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

plt.show()




