import requests
from lxml import etree
from bs4 import BeautifulSoup


# https://www.autohome.com.cn/all/

class qczj():
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User - Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('成功')
            content = response.content
            # content_str = content.decode('gb2312')
            self.pares_noval_data(content)

    def pares_noval_data(self, htmlData):
        # print(htmlData)
        x_html = etree.HTML(htmlData)
        li_list = x_html.xpath('//div[@id="auto-channel-lazyload-article"]/ul/li')
        print(len(li_list))
        for lis in li_list:
            for li in lis:
                # print(type(li))
                cat_info = {}
                # 图片
                cat_info['img'] = 'https:' + li.xpath('.//div[@class="article-pic"]/img/@src')[0]
                # 标题
                cat_info['title'] = li.xpath('.//h3/text()')[0]
                # 时间
                cat_info['time'] = li.xpath('.//div[@class="article-bar"]/span[1]/text()')[0]
                # 浏览量
                cat_info['page view'] = li.xpath('.//div[@class="article-bar"]/span[2]/em[1]/text()')[0]
                # 评论
                cat_info['Comment'] = li.xpath('.//div[@class="article-bar"]/span[2]/em[2]/text()')[0]
                # 内容
                cat_info['article'] = li.xpath('.//p/text()')[0]
                print(cat_info)



if __name__ == '__main__':
    start_url = 'https://www.autohome.com.cn/all/'
    qidianspider = qczj()
    qidianspider.start_request(start_url)
