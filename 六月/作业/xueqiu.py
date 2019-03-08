# 头条 -1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json
# ?since_id=-1&max_id=-1&count=10&category=-1
# 直播 6
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=6
# 沪深 105
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=105
# 房产 111
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=111
# 港股 102
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=102
# 基金 104
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=104
# 美股 101
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=101
# 私募 113
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=113
# 汽车 114
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=114
# 保险 110
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=110

# {
# 'since_id':'-1',
# 'max_id':'-1',
# 'count':'10',
# 'category':'6'
# }

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20325295&count=15&category=-1

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20325280&count=15&category=-1
# next_id: 20325263
# next_max_id: 20325264

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20325264&count=15&category=-1
# next_id: 20325248
# next_max_id: 20325249

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20325249&count=15&category=-1

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20325249&count=15&category=-1

# 直播
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=6
# next_id: 814129
# next_max_id: 814130

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=814130&count=15&category=6

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=814130&count=15&category=6

from urllib import request, error, parse
import json, ssl
import pymysql
from w3lib.html import remove_tags
import time, datetime


def xueqiu_spider():
    base_url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?'
    # 头条 -1  直播 6 沪深 105 房产 111 港股 102 基金 104 美股 101
    # 私募 113 汽车 114 保险 110
    # https://xueqiu.com/v4/statuses/public_timeline_by_category.json
    # ?since_id=-1&max_id=-1&count=10&category=-1
    category_list = ['-1', '6', '105', '111', '102', '104', '101', '113', '114', '110']
    for category in category_list:
        parmas = {
            'since_id': '-1',
            'max_id': '-1',
            'count': '10',
            'category': category
        }
        start_requests(base_url, parmas)


def start_requests(base_url, parmas):
    """
    根据参数和url地址构建完整链接，发起请求
    :param base_url:
    :param parmas:
    :return:
    """
    # urlencode将字典中的参数转为url编码格式的字符串
    parmas_str = parse.urlencode(parmas)
    # print(parmas_str)
    # 完整的url地址
    full_url = base_url + parmas_str
    print(full_url)
    # 构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Cookie': 'aliyungf_tc=AQAAAFqMaEZuUQEAi/OUPUPS22LfPOjH; xq_a_token=0d73a36f00a0e985d381412742c39d12fb3ca56a; xq_a_token.sig=knknlVAPG2nkQ9enLy6gnEylv5w; xq_r_token=18d38484159ce73ae3451797d6517a41efa531b1; xq_r_token.sig=_SVEXsDz6FhNpFjXlGS8TPj_T7Q; _ga=GA1.2.2016846595.1550727345; _gid=GA1.2.1301339519.1550727345; Hm_lvt_1db88642e346389874251b5a1eded6e3=1550727345; u=571550727346398; device_id=5414a810d3b9f5d82a33832aea74e4b4; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1550727459'
    }
    context = ssl._create_unverified_context()
    # 构建一个request
    req = request.Request(full_url, headers=headers)
    # 发起请求
    try:
        response = request.urlopen(req, timeout=10, context=context)
        if response.status == 200:
            print('请求成功', )
            jsonData = response.read().decode('utf-8')
            parse_list_data(jsonData, parmas['category'])
    except error.HTTPError as err:
        print('111', err.reason)
    except error.URLError as err:
        print('222', err.reason)


def parse_list_data(jsonData, category):
    # 将json字符串转换为python数据类型
    data = json.loads(jsonData)
    # print(type(data),data)
    data_list = data['list']
    for info in data_list:
        info_data = info['data']
        info_data = json.loads(info_data)
        # print(info_data)

        article = {}
        article['category'] = category
        if category == '6':
            # 说明是直播
            # 标题
            article['title'] = '暂无'
            # 内容
            article['content'] = info_data['text']
            # 来源
            article['db_source'] = '暂无'
            # 阅读量
            article['view_count'] = info_data['view_count']
            # 发布时间
            article['created_at'] = info_data['created_at']

        else:
            # 说明是其他分类
            # 标题
            article['title'] = info_data['title']
            # 内容 remove_tags去除字符串中包含的html标签
            article['content'] = remove_tags(info_data['description'])
            # 来源
            article['db_source'] = info_data['user']['screen_name']
            # 阅读量
            article['view_count'] = int(info_data['view_count'])
            # 发布时间
            article['created_at'] = info_data['created_at']
            # dateArray = datetime.datetime.utcfromtimestamp(created_at)
            # otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")


        insert_sql = """
            INSERT INTO xueqiu(%s)
            VALUES(%s)
            """ % (','.join(info.keys()), ','.join(['%s'] * len(info)))

        try:
            my_cursor.execute(insert_sql, list(info.values()))
            mysql_con.commit()
            print('数据插入成功')
        except Exception as err:
            print(err)
            mysql_con.rollback()

    # step1：将数据存储到数据库
    # step2:将其他分页数据也获取到


if __name__ == '__main__':
    mysql_con = pymysql.Connect(
        '127.0.0.1', 'root', '123',
        'xueqiu', 3306, charset='utf8'
    )

    my_cursor = mysql_con.cursor()
    xueqiu_spider()
