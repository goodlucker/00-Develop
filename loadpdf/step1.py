import time
from time import sleep 
import random  #用于对延时设置随机数，尽量模拟人的行为
import requests  #用于向网站发送请求
from lxml import etree    #lxml为第三方网页解析库，强大且速度快

url = 'https://www.lexjansen.com/cgi-bin/xsl_transform.php?x=pharmasug-cn2024'

# User-Agent Header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers, timeout=10)
html = response.text  
print(html)