#-*- coding:utf-8 -*-
import pandas as pd #通常采用pd表示pandas

#创建一个序列
s = pd.Series([1,2,3],index=['a','b','c'])
#创建一个表
d = pd.DataFrame([[1,2,3],[4,5,6]],columns = ['a','b','c'])