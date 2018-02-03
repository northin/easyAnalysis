# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 16:52:16 2018

@author: Administrator
"""
import pandas as pd
import numpy as np

a1 = pd.read_excel(u'./data/gflist.xlsx')


b = a1[u'歌曲id']
c = b.value_counts()
c.name = u'歌曲数量'

d = pd.DataFrame(c)

d[u'歌曲id'] = d.index



e = pd.merge(d,a1,on=[u'歌曲id'])



f = e.drop_duplicates([u'歌曲id'])

f.index =  np.arange(45640)
g = f[f[u'歌曲数量']>100]

with open('gftop.json', 'w') as f:
  f.write(g.to_json(orient='index',force_ascii=False))



