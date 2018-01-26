# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import pandas as pd

df = pd.read_excel(u'./data/content1.xlsx')

df2 = pd.read_excel(u'./data/content2.xlsx')

m1 = pd.read_excel(u'./data/music1.xlsx')
m2 = pd.read_excel(u'./data/music2.xlsx')
m3 = pd.read_excel(u'./data/music3.xlsx')

a1 = pd.read_excel(u'./data/album.xlsx')

s1 = pd.read_excel(u'./data/artist.xlsx')

m4 = pd.concat([m1,m2,m3])
df3 = pd.concat([df,df2])

#df4 = df3.groupby(u'评论数').mean();

#df5 = df4.sort_index(ascending=False)

df6 = df3.sort_values(by=u"评论数",ascending=False)[0:10]


df7 = pd.merge(df6,m4,on=[u"歌曲id"])

df8 = pd.merge(df7,a1,on=[u"专辑id"])

df9 = pd.merge(df8,s1,on=[u'歌手id'])
df10 = df9.to_json(orient='index',force_ascii=False)
print(df10)
with open('testjson1.json', 'w') as f:
  f.write(df10)
