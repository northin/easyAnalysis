# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:28:19 2018

@author: Administrator
"""

import numpy as np

import pandas as pd

df = pd.read_excel(u'./data/content1.xlsx')

df3 = pd.read_excel(u'./data/content2.xlsx')

m1 = pd.read_excel(u'./data/music1.xlsx')
m2 = pd.read_excel(u'./data/music2.xlsx')
m3 = pd.read_excel(u'./data/music3.xlsx')

a1 = pd.read_excel(u'./data/album.xlsx')

s1 = pd.read_excel(u'./data/artist1.xlsx')

m4 = pd.concat([m1,m2,m3])
df4 = pd.concat([df,df3])


df5 = df4[df4[u'评论数']> 10000]

df6 = pd.merge(df5,m4,on=[u'歌曲id'])

df7 = pd.merge(df6,a1,on=[u"专辑id"])

df2 = pd.merge(df7,s1,on=[u'歌手id'])



dfChina = df2[df2[u'分类id']<1004].count()[u"歌曲id"]


dfEUAM = df2[(df2[u'分类id']>1004)&(df2[u'分类id']<2004)].count()[u"歌曲id"]


dfJP = df2[(df2[u'分类id']>5004)&(df2[u'分类id']<6004)].count()[u"歌曲id"]


dfKO = df2[(df2[u'分类id']>6004)&(df2[u'分类id']<7004)].count()[u"歌曲id"]

dfANO = df2[(df2[u'分类id']>3004)&(df2[u'分类id']<4004)].count()[u"歌曲id"]


dfList = [[dfChina,'华语中国'],[dfEUAM,'欧美'],[dfJP,'日本'],
          [dfKO,'韩国'],[dfANO,'其他']]

data = pd.DataFrame(dfList,columns=["歌曲数",'语种地区'])





