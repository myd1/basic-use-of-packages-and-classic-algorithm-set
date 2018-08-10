#-*- coding:utf-8 -*-
import pandas as pd

#参数初始化
filename='E:\\3data-mining\\2py-testing\\data and code\\chapter5\\demo\\data\\bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,: 8].as_matrix()
y = data.iloc[:,8].as_matrix()

#从sklearn包中导入逻辑回归模型
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x,y) #训练模型
rlr.get_support() #获取特征筛选结果
print(u'通过随机逻辑回归模型筛选特征结果')
print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support(indices=True)]))
x = data[data.columns[rlr.get_support(indices=True)]].as_matrix() #筛选好特征
lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print(u'逻辑回归模型训练结束')
print(u'模型的平均正确率：%s' % lr.score(x, y)) #给出模型的正确率
