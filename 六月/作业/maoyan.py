from urllib import request, parse, error
import json, re
import pymysql


# https://maoyan.com/board/4?offset=0

def maoyan_spider():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入截止页码:'))

    for page in range(start_page, end_page + 1):
        parmas = {
            'offset': (page - 1) * 10
        }
        b_data = send_request('https://maoyan.com/board/4?', parmas)
        parse_page_data(b_data)


def send_request(url, parmas=None):
    if parmas:
        parmas = parse.urlencode(parmas)
        url = url + parmas
        # print(url)

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    req = request.Request(url, headers=req_headers)
    response = request.urlopen(req)
    if response.status == 200:
        print("请求成功")
        b_data = response.read()
        return b_data


def parse_page_data(b_data):
    html = b_data.decode('utf-8')
    # print(html)
    pattern9 = re.compile(
        '<dd.*?<i.*?board-index.*?>(.*?)</i>.*?' +
        '<img.*?data-src="(.*?)".*?>.*?' +
        '<p.*?name.*?>.*?<a.*?>(.*?)</a>.*?' +
        '<p.*?star.*?>(.*?)</p>.*?' +
        '<p.*?releasetime.*?>(.*?)</p>.*?' +
        '<i.*?>(.*?)</i>.*?' +
        '<i.*?>(.*?)</i>',
        re.S
    )
    result9 = re.findall(pattern9, html)
    # print(result9)
    for i in result9:
        print(i)

    return result9



# def save_userinfo_to_db(info):
#     insert_sql = """
#     INSERT INTO my(%s)
#     VALUES(%s)
#     """ % (','.join(info.keys()), ','.join(['%s'] * len(info)))
#
#     try:
#         my_cursor.execute(insert_sql, list(info.values()))
#         mysql_con.commit()
#         print('数据插入成功')
#     except Exception as err:
#         print(err)
#         mysql_con.rollback()


if __name__ == '__main__':
    # mysql_con = pymysql.Connect(
    #     '127.0.0.1', 'root', '123',
    #     'maoyan', 3306, charset='utf8'
    # )
    #
    # my_cursor = mysql_con.cursor()
    maoyan_spider()
