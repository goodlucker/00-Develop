 #分析网页后可以得知get历史所有数据的参数
url='https://datachart.500.com/ssq/history/newinc/history.php?start=03001'  

#加载相关的库
import requests
import numpy as np
import pandas as pd

#获取历史所有双色球数据
response = requests.get(url)
response.encoding = 'utf-8'  
re_text = response.text

#网页数据解析
re=re_text.split('<tbody id="tdata">')[1].split('</tbody>')[0]
result=re.split('<tr class="t_tr1">')[1:]

all_numbers=[]
for i in result:
    each_numbers=[]
    i=i.replace('<!--<td>2</td>-->','')
    each=i.split('</td>')[:-1]
    for j in each:
        each_numbers.append(j.split('>')[1].replace('&nbsp;',''))
    
    all_numbers.append(each_numbers)
  
#定义列名称  
col=['期号','红球1','红球2','红球3','红球4','红球5','红球6','蓝球','快乐星期天','奖池奖金(元)',
     '一等奖注数','一等奖奖金(元)','二等奖注数','二等奖奖金(元)','总投注额(元)','开奖日期']

#解析完网页数据，生成双色球数据框
df_all=pd.DataFrame(all_numbers,columns=col)
df_all.head()