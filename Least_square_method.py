"""
最小二乘法：通过残差平方和最小来优化回归的结果
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import leastsq #导入最小二乘法算法
#from skimage import io, color
from pylab import mpl #实现中文的输出

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
"""
设置数据：样本数据和真实数据
"""
##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])
Yi=np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])
'''
    设定拟合函数和偏差函数
    函数的形状确定过程：
    1.先画样本图像
    2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
'''
##需要拟合的函数func :指定函数的形状
def func(p,x):
    k,b=p
    return k*x+b

#偏差函数：x，y都是列表
def error(p,x,y):
    return func(p,x)-y
'''
    主要部分：附带部分说明
    1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
    2.官网的原话（第二个值）：Value of the cost function at the solution
    3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
    4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
'''
#k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0=[1,20]
#把error函数中除了p0以外的参数打包到args中(使用要求)
Para=leastsq(error,p0,args=(Xi,Yi)) #调用python中自带的函数
k,b = Para[0]
print("k=",k,"b=",b)
print("cost:"+str(Para[1]))
print("求解的拟合直线为：")
print("y="+str(round(k,2))+"x"+str(round(b,2))) #str() 函数将对象转化为适于人阅读的形式。 round() 方法返回浮点数x的四舍五入值。
#print("y=" + k + "x" + b) #上面是本语句的格式化输出
'''
   绘图，看拟合效果.
   matplotlib默认不支持中文，label设置中文的话需要另行设置
   如果报错，改成英文就可以
'''
#画样本点
plt.figure(figsize=(6,4))  #指定图像比例为8：6
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2) #scatter画散点图

#画拟合曲线
x = np.linspace(0,12,100) #在0-12之间直接画100个点
y=k*x+b
plt.plot(x,y,color ="red",label="拟合数据",linewidth=2)
plt.legend(loc='lower right') #绘制图例
plt.savefig("LEAST SQUARE.jpg") #应该在show()之前进行调用，在之后的话会重新创建一个的
plt.show()







