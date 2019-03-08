from selenium import webdriver
import time
from lxml import etree
import string


class duobanSpider(object):
    def __init__(self):
        self.brower = webdriver.Chrome(
            executable_path='/home/lrx/桌面/chromedriver'
        )
        self.brower.get('https://movie.douban.com/')
        self.brower.find_element_by_id('inp-query').send_keys('成龙')
        self.brower.find_element_by_class_name('inp-btn').click()
        print('搜索完成')
        self.get_live_data(self.brower.page_source)

        time.sleep(1)
        self.brower.find_element_by_id('inp-query').clear()
        self.brower.find_element_by_id('inp-query').send_keys('周星驰')
        self.brower.find_element_by_class_name('inp-btn').click()
        print('搜索完成')
        self.get_live_data(self.brower.page_source)

    def get_live_data(self, html_data):
        # print(html_data)
        div_lis = self.brower.find_elements_by_xpath('//div[@class="item-root"]')
        del div_lis[0]
        # print(div_lis)

        for div_ls in div_lis:

            live_dict = {}
            # 获取封面图
            live_dict['coverImage'] = div_ls.find_element_by_xpath('.//img[@class="cover"]').get_attribute('src')
            live_dict['name'] = div_ls.find_element_by_xpath('.//a[@class="title-text"]').text
            live_dict['score'] = div_ls.find_element_by_xpath('.//div[@class="rating sc-bwzfXH hxNRHc"]/span[2]').text
            # live_dict['comment'] = div_ls.find_element_by_xpath('.//div[@class="rating sc-bwzfXH hxNRHc"]/span[3]').text
            live_dict['type'] = div_ls.find_element_by_xpath('.//div[@class="meta abstract"]').text
            live_dict['actor'] = div_ls.find_element_by_xpath('.//div[@class="meta abstract_2"]').text
            # live_dict['name1'] = div_ls.find_element_by_xpath('.//div[@class="title"]/span[1]').text
            # live_dict['name2'] = div_ls.find_element_by_xpath('.//div[@class="title"]/span[2]').text
            print(live_dict)




if __name__ == '__main__':
    duobanSpider()
