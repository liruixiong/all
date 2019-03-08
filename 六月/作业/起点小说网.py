import requests
from lxml import etree


# https://www.qidian.com/all
# https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2
# https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3
# https://www.qidian.com/all?page=2

class QidainSpider():
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User - Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            self.pares_noval_data(response.text)
            print('成功')

    def pares_noval_data(self, htmlData):
        # print(htmlData)
        # 把 HTML 文档转换为xpsth
        x_html = etree.HTML(htmlData)
        # 获取页面的小说列表
        li_list = x_html.xpath('//ul[@class="all-img-list cf"]/li')
        # print(len(li_list))
        # 遍历，获取每一本小说的内容
        for li in li_list:
            # print(type(li))
            book_info = {}
            # 封面图片(去标签的属性@属性明)
            book_info['coverImage'] = 'https:' + li.xpath('./div[@class="book-img-box"]//img/@src')[0]
            # 标题(取标签的文本使用text())
            book_info['title'] = li.xpath('./div[@class="book-mid-info"]/h4/a/text()')[0]
            # 作者
            book_info['author'] = li.xpath('.//p[@class="author"]/a[@class="name"][1]/text()')[0]
            # 分类
            book_info['categroy'] = li.xpath('.//p[@class="author"]/a[2]/text()')[0] + \
                                    li.xpath('.//p[@class="author"]/i/text()')[0] + \
                                    li.xpath('.//p[@class="author"]/a[3]/text()')[0]
            # 连载状态
            book_info['statu'] = li.xpath('.//p[@class="author"]/span/text()')[0]
            # 内容
            book_info['article'] = li.xpath('.//p[@class="intro"]/text()')[0].replace(' ', '').replace('\r', '')

            print(book_info)
            end_url = 'https:' + li.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0] + '#Catalog'
            print(end_url)
            html = self.send_book_detail_request(end_url)
            self.parse_chpater_list(html)

        # next_page = x_html.xpath('//a[@class="lbf-pagination-next "]/@href')
        # if len(next_page) > 0:
        #     next_page = 'https:' + next_page[0]
        #     # 继续请求
        #     self.start_request(next_page)
        # else:
        #     print("数据获取完毕")

    def send_book_detail_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print('书籍详情请求成功')
            return response.text

    def parse_chpater_list(self, html):
        # 实例化一个xpath的解析对象
        x_html = etree.HTML(html)

        # 提取章节目录
        div_volume = x_html.xpath('.//div[@class="volume"]')

        if len(div_volume) > 0:
            print('说明是静态页面')
            for div in div_volume:
                isFree = div.xpath('./h3/span/text()')[0].replace(' ', '')
                if '免费' in isFree:
                    print('这个div存放的免费章节')
                    chpater_lis = div.xpath('./ul[@class="cf"]/li')
                    for chpater_li in chpater_lis:
                        chpater_url = 'https:' + chpater_li.xpath('./a/@href')[0]
                        # print(chpater_url)
                        html = self.send_book_detail_request(chpater_url)
                        self.parse_chpater_detail(html)

    def parse_chpater_detail(self, html):

        x_html = etree.HTML(html)
        chpaterInfo = {}
        # 章节标题
        chpaterInfo['title'] = x_html.xpath('//h3[@class="j_chapterName"]/text()')[0]
        # 书籍名称
        chpaterInfo['novalTitle'] = x_html.xpath('//div[@class="info fl"]/a[1]/text()')[0]
        # 书籍内容
        chpaterInfo['content'] = ''.join(x_html.xpath('//div[@class="read-content j_readContent"]/p/text()')).replace(
            '\u3000', '')

        print(chpaterInfo)





if __name__ == '__main__':
    start_url = 'https://www.qidian.com/all'
    qidianspider = QidainSpider()
    qidianspider.start_request(start_url)
