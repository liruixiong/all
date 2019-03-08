from urllib import request, parse
import json, re ,ssl
import pymysql


# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325311&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325296&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325281&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325265&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325250&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20325250&count=15&category=-1


# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=6
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=814156&count=15&category=6
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=814081&count=15&category=6

def xueqiu_spider():
    response = send_requests('https://xueqiu.com/#/livenews')
    parse_page_data(response.read())


def send_requests(url, parmas=None):
    if parmas:
        parmas = parse.urlencode(parmas)
        url = url + parmas

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    req = request.Request(url, headers=req_headers)
    # print(url)
    response = request.urlopen(req)
    if response.status == 200:
        print('请求成功')

        return response


def parse_page_data(b_data):
    html = b_data.decode('utf-8')
    print(html)


if __name__ == '__main__':
    xueqiu_spider()
