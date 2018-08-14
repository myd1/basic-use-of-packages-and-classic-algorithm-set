#-*- coding: utf-8 -*-
#使用ID3决策树算法预测销售量高低
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
#导入数据
inputfile='E:\\3data-mining\\2py-testing\\data and code\\chapter5\\demo\\data\\sales_data.xls'
data = pd.read_excel(inputfile, index_col = u'序号') #导入数据

#数据为类别标签，将其转化为数据
#用1来表示好是高，用-1表示坏否低
data[data==u'好'] = 1
data[data==u'是'] = 1
data[data==u'高'] = 1
data[data !=1 ] = -1

#读取数据
x = data.iloc[:,:3].as_matrix().astype(int)  ##行全选，列选下标0-3
y = data.iloc[:,3].as_matrix().astype(int)
#print(x)
#print(y)
#建立模型
dtc = DTC(criterion='entropy') #基于信息熵建立决策树
#训练模型
dtc.fit(x,y)
#导入的文件为dot文件，因此需要安装Grapevine才能转化为PDF和png格式
from sklearn.tree import export_graphviz
x = pd.DataFrame(x)
from sklearn.externals.six import StringIO
x = pd.DataFrame(x)
with open("tree.dot", 'w') as f:
  f = export_graphviz(dtc, feature_names = x.columns, out_file = f)


