# 什么是pyquery？

# 是jquery的python的python实现，同样可以从html文档中提取数据
# ，易用性和解读行都很好。

# 安装：pip3 install pyquery

from pyquery import PyQuery

"""
find(selector) : 使用css选择器查找
filter(selector) : 根据id或者class过滤节点
直接对pyquery对象使用css选择器查找节点
.eq(index) : 根据索引获取指定的节点（从0开始）
.text(): 获取节点的文本
.attr('属性名') ：获取节点的属性
"""

# 糗事百科
# 目标url：https://www.qiushibaike.com/textnew/
import requests, pymongo
# exceptions来做异常处理
from requests import exceptions


def qioshi():
    start_url = 'https://www.qiushibaike.com/textnew/'
    staet_request(start_url)


def staet_request(start_url):
    html = send_request(start_url)
    if html:
        nextUrl = parse_page_data(html)
        if nextUrl:
            staet_request(nextUrl)
    else:
        print('当前URL请求失败')


def send_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print('成功')
            return response.text
    except exceptions.RequestException as err:
        print(err, '请求错误')
    except exceptions.HTTPError as err:
        print(err, 'HTTPError')
    return None


def parse_page_data(html):
    pq_html = PyQuery(html)
    # print(pq_html)
    article_divs = pq_html.find('div#content-left > div')
    # article_div=pq_html.find('div').filter('#content-left').find('#content-left').filter('.article block untagged mb15')
    # article_div=pq_html.find('div').filter('.article block untagged mb15')
    # print(type(article_divs))

    for article_div in article_divs.items():
        # print(type(article_div))
        article = {}
        # article['name'] = article_div('div.author.clearfix a').eq(1).attr('title')
        article['name'] = article_div('div.author.clearfix a').eq(1)('h2').text()
        article['content'] = article_div('a.contentHerf span').eq(0)('span').text()
        article['page view'] = article_div('span.stats-vote ').text()
        article['Comment'] = article_div('span.stats-comments a').eq(0).text()
        print(article)
    nextUrl = pq_html('span.next').parent().attr('href')
    if nextUrl:
        nextUrl = 'https://www.qiushibaike.com/textnew/' + nextUrl
        print(nextUrl)
        return nextUrl
    else:
        print('结束了')
        return None


if __name__ == '__main__':
    qioshi()
