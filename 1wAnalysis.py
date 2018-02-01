# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:28:30 2018

@author: Administrator
"""
import sys

# 设置环境为utf-8编码格式，防止处理中文出错
reload(sys)
#sys.setdefaultencoding('utf-8')
import numpy as np

import pandas as pd
import jieba.posseg as psg
from collections import Counter
#df = pd.read_excel(u'./data/content1.xlsx')

#df3 = pd.read_excel(u'./data/content2.xlsx')

#df4 = pd.concat([df,df3])


#df5 = df4[df4[u'评论数']> 10000]


#df6 = df5[[u'热评内容',u'歌曲id']]


#file = open('analysis.txt','wb')
#indexList = df6[u'歌曲id'].get_values()
#for i in indexList:
#    file.write(df8[df8[u'歌曲id']==i][u'热评内容'].get_values()[0])
#file.close()
     

#comments_text = open('analysis1.txt').read()

# 词    词性
#comments_words_with_attr = [(x.word,x.flag) for x in psg.cut(comments_text) if len(x.word) >= 2] 
# 这里的x.word为词本身，x.flag为词性

#with open('out1.txt','w+') as f:
 #   for x in comments_words_with_attr:
 #       f.write('{0}\t{1}\n'.format(x[0],x[1])) #
 
                
comments_words_with_attr = []
#with open('out1.txt','r') as f:
#    for x in f.readline():
#        print(x)
        #pair = x.split()
        #print(pair)
        #comments_words_with_attr.append((pair[0],pair[1]))
  
f = open('out1.txt','r')

for i in range(0,706381):
    print(i)
    pair = f.readline().split();
    comments_words_with_attr.append((pair[0],pair[1]))

filter_attr = []

words = [x[0] for x in comments_words_with_attr if x[1] not in filter_attr]

# {词:词性}                
attr_dict = {}
for x in comments_words_with_attr:
    attr_dict[x[0]] = x[1]                
                
                
                
                
c = Counter(words).most_common(1000)
with open('most.txt','w+') as f:
    for x in c:
        f.write('{0},{1},{2}\n'.format(x[0],x[1],attr_dict[x[0]]))               
                
                
                
                
                
                
                