# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:28:30 2018

@author: Administrator
"""

import numpy as np

import pandas as pd

df = pd.read_excel(u'./data/content1.xlsx')

df3 = pd.read_excel(u'./data/content2.xlsx')

df4 = pd.concat([df,df3])


df5 = df4[df4[u'评论数']> 10000]


df6 = df5[u"热评内容"]







