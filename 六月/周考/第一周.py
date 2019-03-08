import requests
from lxml import etree
import pymysql, pymongo
from requests import exceptions


class liania():
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # self.pares_noval_data(response.text)
            self.pares_one_data(response.text)
            self.pares_two_data(response.text)

    def pares_two_data(self,html_data):
        one_html = etree.HTML(html_data)
        next_page = one_html.xpath('//div[@class="nav typeUserInfo"]/ul/li[3]/a/@href')[0]
        print(next_page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(next_page, headers=headers)
        if response.status_code == 200:
            print('租房请求成功')
            self.pares_renting_data(response.text)


    def pares_renting_data(self,htmlData):
        # print(htmlData)
        x_html = etree.HTML(htmlData)
        li_list = x_html.xpath('//div[@class="content__list--item"]')
        # print(len(li_list))
        for li in li_list:
            renting_info = {}
            renting_info['title'] = li.xpath('.//p[@class="content__list--item--title twoline"]/a/text()')[0].replace(' ', '').replace('\n', '')
            renting_info['address'] = li.xpath('.//p[@class="content__list--item--des"]/a[1]/text()')[0] + '-' + li.xpath('.//p[@class="content__list--item--des"]/a[2]/text()')[0]
            renting_info['time'] = li.xpath('.//p[@class="content__list--item--time oneline"]/text()')[0]
            renting_info['name'] = li.xpath('.//p[@class="content__list--item--brand oneline"]/text()')[0].replace(' ', '').replace('\n', '')
            renting_info['money'] = li.xpath('.//span[@class="content__list--item-price"]/em/text()')[0] + li.xpath('.//span[@class="content__list--item-price"]/text()')[0]


            print(renting_info)

    def pares_one_data(self, htmldata):
        one_html = etree.HTML(htmldata)
        next_page = one_html.xpath('//div[@class="nav typeUserInfo"]/ul/li[1]/a/@href')[0]
        print(next_page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(next_page, headers=headers)
        if response.status_code == 200:
            # self.pares_noval_data(response.text)
            print('二手房请求成功')
            self.pares_noval_data(response.text)


    def pares_noval_data(self, htmlData):
        # print(htmlData)
        x_html = etree.HTML(htmlData)
        li_list = x_html.xpath('//li[@class="clear LOGCLICKDATA"]')
        # print(len(li_list))
        for li in li_list:
            # print(type(li))
            book_info = {}
            book_info['title'] = li.xpath('./div[@class="info clear"]/div/a/text()')[0]
            book_info['name'] = li.xpath('.//div[@class="address"]/div/a/text()')[0]
            book_info['divide'] = li.xpath('.//div[@class="address"]/div[1]/text()')[0]
            book_info['square'] = li.xpath('.//div[@class="address"]/div/text()[2]')[0]
            book_info['direction'] = li.xpath('.//div[@class="address"]/div/text()[3]')[0]
            book_info['Paperback'] = li.xpath('.//div[@class="address"]/div/text()[4]')[0]
            book_info['Elevator'] = li.xpath('.//div[@class="address"]/div/text()[5]')[0]
            book_info['floor'] = li.xpath('.//div[@class="flood"]/div/text()[1]')[0]
            book_info['year'] = li.xpath('.//div[@class="flood"]/div/text()[2]')[0]
            book_info['suer_name'] = li.xpath('.//div[@class="flood"]/div/a/text()')[0]
            book_info['followInfo'] = li.xpath('.//div[@class="followInfo"]/text()[1]')[0]
            book_info['look'] = li.xpath('.//div[@class="followInfo"]/text()[2]')[0]
            book_info['money'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0] + '万'
            book_info['suer_money'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0]
            print(book_info)
            # next_page = x_html.xpath('//div[@class="page-box house-lst-page-box"]/a[5]/@href')
            # if len(next_page) > 0:
            #     next_page = 'https:' + next_page[0]
            #     # 继续请求
            #     self.start_request(next_page)
            # else:
            #     print("数据获取完毕")


if __name__ == '__main__':
    start_url = 'https://bj.lianjia.com'
    qidianspider = liania()
    qidianspider.start_request(start_url)
