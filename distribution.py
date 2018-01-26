# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:11:44 2018

@author: Administrator
"""

import numpy as np

import pandas as pd

df = pd.read_excel(u'./data/content1.xlsx')

df2 = pd.read_excel(u'./data/content2.xlsx')

df3 = pd.concat([df,df2])

#1w
df4 = df3[df3[u'评论数']>10000]

df10000 = df4.count()[u"歌曲id"]



df6000 = df3[(df3[u'评论数']>6000)&(df3[u'评论数']<=10000)].count()[u'歌曲id']


df2000 = df3[(df3[u'评论数']>2000)&(df3[u'评论数']<=6000)].count()[u'歌曲id']


df1000 = df3[(df3[u'评论数']>1000)&(df3[u'评论数']<=2000)].count()[u'歌曲id']

df500 = df3[(df3[u'评论数']>500)&(df3[u'评论数']<=1000)].count()[u'歌曲id']

df100 = df3[(df3[u'评论数']>0)&(df3[u'评论数']<=500)].count()[u'歌曲id']

df0 = 2468736 - 1734451

dfList = [[df10000,'10000以上'],[df6000,'6000-10000'],[df2000,'2000-6000'],
          [df1000,'1000-2000'],[df500,'500-1000'],[df100,'0-500'],[df0,'0']]

data = pd.DataFrame(dfList,columns=["歌曲数",'评论范围'])

