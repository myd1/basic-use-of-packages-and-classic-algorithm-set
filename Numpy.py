#-*- coding= utf-8 -*-
# numpy基本操作
import numpy as np #创建numpy别名
a = np.array([2,1,3,4,5,1,6,7])
#输出该数组
# sorting
a.sort()
print(a)

#对前三个数字进行切片
print(a[:3])
#对后面的数据进行输出
print(a[-3:])
#进行逆序输出#################
b = a[::-1]
print(b)
################################

#output min
print(a.min())
# sorting
print(a.sort())
#creating two array
b = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(b)
print(b*b)