import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}
url = "http://www.tianqihoubao.com/lishi/zhengzhou/month/202004.html"

res = requests.get(url,headers=headers)
html =  res.content.decode('gbk')
#print(html.text)
soup = BeautifulSoup(html,'lxml')
list = soup.find_all('tr')
#print(list)
dates,conditions,temp = [],[],[]
for i in list[1:]:              #从第二列开始是天气数据
    data = i.text.split()       #对文字内容进行分段
    #print(data)
    #data[0] = ['2020年04月01日', '阴', '/阴', '13℃', '/', '7℃', '东北风', '3-4级', '/东北风', '3-4级']
    dates.append(data[0])
    conditions.append(data[1:3])
    temp.append(data[3:6])
#print(dates,conditions,temp)
data_mouth = pd.DataFrame()      #通过pandas创建一个数据集，存放天气信息
data_mouth['日期'] = dates
data_mouth['天气情况'] = conditions
data_mouth['气温'] = temp

print(data_mouth)

data_mouth.to_csv("郑州天气.csv",index=False,encoding='utf-8') #导入到csv文件，不保留行索引
