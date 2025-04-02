import requests
from bs4 import BeautifulSoup
import os
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def download_pdf(url, output_folder):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # 使用 requests.Session 对象并配置重试策略
    session = requests.Session()
    retry = Retry(
        total=10, 
        connect=10, 
        read=10, 
        redirect=10, 
        backoff_factor=2, 
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    try:
        # 获取网页内容
        response = session.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return

    # 解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 找到所有的<a>标签，提取href属性
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]
    
    if not pdf_links:
        print(f"在{url}中没有找到PDF链接")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 下载每个PDF文件
    for pdf_link in pdf_links:
        pdf_url = pdf_link if pdf_link.startswith('http') else f"{url}/{pdf_link}"
        try:
            pdf_response = session.get(pdf_url, headers=headers)
            pdf_response.raise_for_status()  # 检查请求是否成功

            pdf_file_name = os.path.join(output_folder, os.path.basename(pdf_url))
            with open(pdf_file_name, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"{pdf_file_name} 下载成功")
            
            # 在下载每个PDF文件后，添加一个小延时
            time.sleep(3)  # 增加延时以减少对服务器的压力
        except requests.exceptions.RequestException as e:
            print(f"无法下载 {pdf_url}: {e}")

if __name__ == '__main__':
    # 指定要下载的网页URL
    url = 'https://www.lexjansen.com/cgi-bin/xsl_transform.php?x=pharmasug-cn2024'
    output_folder = 'D:\CRM-L460\D-disk\98_App\Scripts\loadpdf\pharmasugcn-2024'
    
    download_pdf(url, output_folder)

