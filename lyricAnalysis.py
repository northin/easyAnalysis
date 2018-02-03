# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 13:25:08 2018

@author: Administrator
"""


import numpy as np
import pandas as pd
import jieba.posseg as psg
from collections import Counter
import sys

# 设置环境为utf-8编码格式，防止处理中文出错
reload(sys)
sys.setdefaultencoding('utf-8')
df1 = pd.read_excel(u'./data/gfmusic.xlsx')

#15048  没有歌词
df2 =  df1[df1[u'歌词'] != 'null']

#获取所有歌曲list
df3 = df2.get_values()


#写入txt中
#file = open(u'./data/lyric.txt','wb')
#for i in df3:
#    sss = i[1]
#    if type(sss) != type(1.2) and type(sss) != type(1):
#        for j in sss.split('\n'):
#            if j.strip() != '':
#                print(j)
#                if ']' in j:
#                    lyricStr = j[j.index(']')+1:len(j)]
#                    print(lyricStr)
#                    file.write(lyricStr)
#        file.write(u"    ")
#file.close()


#分词
#comments_text = open('./data/lyric.txt').read()

# 词    词性
#comments_words_with_attr = [(x.word,x.flag) for x in psg.cut(comments_text) if len(x.word) >= 2] 
# 这里的x.word为词本身，x.flag为词性

#with open('outLyric.txt','w+') as f:
#    for x in comments_words_with_attr:
#        f.write('{0}\t{1}\n'.format(x[0],x[1])) #


#分词结果优化
comments_words_with_attr = []
  
f = open('.data/outLyric.txt','r')

for i in range(0,2749):
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
with open('.data/mostLyric.txt','w+') as f:
    for x in c:
        f.write('{0},{1},{2}\n'.format(x[0],x[1],attr_dict[x[0]])) 











