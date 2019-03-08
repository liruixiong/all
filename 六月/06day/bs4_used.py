#Beautifulsoup4?
# 是python的一个xml和html的解析器，目的是从xml或
# html中提取数据

#安装 pip3 install beautifulsoup4

# beautifulsoup4 要比xpath解析数据要慢，因为beautifulsoup4载入的是
# 整个html文档

"""
findall() 查找所有节点
find() 查找单个
支持css选择器

获取标签的属性 p['class'] => p.attrs['class']
获取标签的文本 p.get_text() => p.string
"""

#腾讯招聘为例
# 首页url地址
#https://hr.tencent.com/position.php

import requests
from bs4 import BeautifulSoup


def tenXunJobSpider():
    start_url = 'https://hr.tencent.com/position.php'
    html = start_request(start_url)
    parse_job_list(html)

def start_request(start_url):
    """
    发起请求
    :param start_url: 目标url地址
    :return:
    """
    #构建请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    }
    response = requests.get(url=start_url,headers=headers)

    if response.status_code == 200:
        print('请求成功')
        html = response.text
        return html

def parse_job_list(htmlData):

    #实例化BeautifulSoup对象
    """
    markup="":html页面源码
    features:制定解析器
    注意：使用BeautifulSoup需要依赖其他解析器
         'lxml' 表示使用的是lxml下的html解析器  容错性好，可读性强
         'html.parser' 是python内置的解析器
    :param htmlData:
    :return:
    """
    html_soup = BeautifulSoup(htmlData,features='lxml')
    """
    name=None, 设置要获取的节点名称
    attrs={}, 是一个字典类型，设置标签的属性
    limit=None, 限制返回的条数
    text 字符串，查找符合text文本的字符串，并返回
    """
    tr_even = html_soup.find_all(name='tr',attrs={'class':'even'})
    tr_odd = html_soup.find_all(name='tr',attrs={'class':'odd'})
    # print(tr_even,tr_odd)

    for tr in tr_even+tr_odd:
        # print(tr)
        #css选择器
        # detail_url = tr.select('.l.square a')[0]['href']
        detail_url = 'https://hr.tencent.com/' + tr.select('.l.square a')[0].attrs['href']
        print(detail_url)
        html = start_request(detail_url)

    




if __name__ == '__main__':
    tenXunJobSpider()