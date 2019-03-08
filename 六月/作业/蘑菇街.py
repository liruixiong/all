from selenium import webdriver
import time
from lxml import etree
import string


class MogujieSpider(object):
    def __init__(self):
        self.mogu = webdriver.Chrome(
            executable_path='/home/lrx/桌面/chromedriver'
        )
        # 使用get方法打开网站
        self.mogu.get(
            'https://market.mogujie.com/?acm=3.mce.1_10_1ksak.128391.0.cNo7hrjgntzQG.pos_0-m_484866-sd_119&ptp=1.n5T00.0.0.esJfW2kq')
        self.get_live_data(self.mogu.page_source)  # 获取页面源码

    def get_live_data(self, html_data):
        # print(html_data)
        time.sleep(1)
        div_lis = self.mogu.find_elements_by_xpath('//div[@class="pc_indexPage_nav_menu fl cube-acm-node has-log-mod"]/ul/li')
        # print(len(div_lis))
        for div_li in div_lis:
            # print(div_li)
            mgj_dict = {}
            mgj_dict['coat'] = div_li.find_element_by_xpath('.//a[@class="catagory color_false maintainHover"]').get_attribute('href')
            print(mgj_dict)



if __name__ == '__main__':
    MogujieSpider()
