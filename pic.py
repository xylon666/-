import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文问题
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data = pd.read_csv("郑州天气.csv")

data['最高气温'] = data['气温'].str.split("'",expand=True)[1]     #extend=True 将数据分为n个纵列，并标记id
data['最低气温'] = data['气温'].str.split("'",expand=True)[5]
# print(data['气温'])
# print(data['最高气温'])
# print(data['最低气温'])

data['最高气温'] = data['最高气温'].map(lambda x:int(x.replace('℃','')))
data['最低气温'] = data['最低气温'].map(lambda x:int(x.replace('℃','')))
#将气温“x℃”转换为数字类型，然后使用pandas里的map函数替换原来的值，方便做Y轴参数
#replace函数，replace(to_replace, value)，将前面的值转化为后面的值

dates = data['日期']
highs = data['最高气温']
lows = data['最低气温']

#画图 配置参数
fig =  plt.figure(dpi=128,figsize=(10,6))   #设定画布分辨率，宽和高
plt.plot(dates,highs,c='red',alpha=0.5)     #alpha 透明度，越接近1越不透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)
#填充highs和lows之间的空隙

#外围标签
plt.title('2020年4月郑州天气情况',fontsize=24)        #标题
plt.xlabel("",fontsize=6)                             #绘制X轴
fig.autofmt_xdate()                                   #绘制斜的目标标签，避免重叠
plt.ylabel("气温",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=10)     #设置坐标轴属性

plt.show()
