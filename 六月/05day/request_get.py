# since_id: -1
# max_id: 20325447
# count: 15
# category: -1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325447&count=15&category=-1

from urllib import request, error, parse
import re, ssl, requests

url = "https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325447&count=15&category=-1"

parmas = {
    'since_id': '-1',
    'max_id': '20325447',
    'count': '15',
    'category': '-1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

reaponse = requests.get(url=url,params=parse,headers=headers)



content = reaponse.content
content_str = content.decode('utf-8')
print(content)
print(content_str)
# text = requests.text
# print(text)

# 获取响应的请求头
response_headers= reaponse.headers
print(response_headers)
# 获取请求头
request_headers = reaponse.request.headers
print(request_headers)
# 获取当前请去偶的UR地址
