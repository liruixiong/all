from urllib import request, parse
import re


def tieba_spider():
    kw = input('请输入搜索贴吧名称:')
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入截止页码:'))

    for page in range(start_page, end_page + 1):
        parmas = {
            'kw': kw,
            'ie': 'utf-8',
            'pn': (page - 1) * 50
        }
        response = send_request('https://tieba.baidu.com/f?', parmas)
        parse_page_data(response.read())


def send_request(url, parmas=None):
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
    pattern = re.compile(
        '<div\sclass="threadlist_title pull_left j_th_tit.*?>' +
        '.*?<a.*?href="(.*?)".*?>(.*?)</a>',
        re.S
    )
    result = re.findall(pattern, html)
    print(result)
    for detailInfo in result:
        print('正在发起' + detailInfo[1] + '请求')
        base_url = 'https://tieba.baidu.com/f?pn=50&kw=%E7%BE%8E%E5%A5%B3&ie=utf-8'
        detail_url = parse.urljoin(base_url, detailInfo[0])
        response = send_request(detail_url)
        parse_detail_data(response.read())


def parse_detail_data(b_data):
    html = b_data.decode('utf-8')
    pattern = re.compile(
        '<img\sclass="BDE_Image"\ssrc="(.*?)".*?>', re.S
    )
    result = re.findall(pattern, html)
    print(result)


if __name__ == '__main__':
    tieba_spider()
