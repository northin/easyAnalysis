# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:42:44 2018

@author: Administrator
"""


import time
import datetime

t = time.time()
import sys
import json
# 设置环境为utf-8编码格式，防止处理中文出错
reload(sys)
#sys.setdefaultencoding('utf-8')
import numpy as np

import pandas as pd

df1 = pd.read_excel(u'./data/qingtian1.xlsx')
df2 = pd.read_excel(u'./data/qingtian2.xlsx')
df3 = pd.read_excel(u'./data/qingtian3.xlsx')
df1 = pd.concat([df1,df2,df3])
df1 = df1[u'日期']
data = []
for i in df1:
    #1517360953287
    dateT = float(i)/float(1000)
    #1517360953.287
    dateData = time.localtime(dateT)
    #20180131
    otherStyleTime = int(time.strftime("%Y%m%d", dateData))
    if len(data) == 0:
        data.append({"date":otherStyleTime,"count":1})
    elif(otherStyleTime>data[len(data)-1]['date']):
        data.append({"date":otherStyleTime,"count":1})
    else:
        data[len(data)-1]['count'] = data[len(data)-1]['count'] + 1
        
data = {'data':data}
j = json.dumps(data)
with open(u'timeqt.json', 'w') as f:
  f.write(j)



