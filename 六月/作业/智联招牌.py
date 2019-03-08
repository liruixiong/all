from selenium import webdriver
import queue,time

import requests
from lxml import etree

from selenium.common.exceptions import NoSuchElementException

class zhilianSpider():
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        self.driver = webdriver.Chrome(
            executable_path='/home/lrx/桌面/chromedriver'
            , options=opt
        )
        self.queue = queue.Queue()

    def start_spider(self, key):

        print('正在获取新的关键字信息', key)

        self.driver.get('https://www.zhaopin.com/')


        self.driver.find_element_by_xpath('//div[@class="risk-warning__content"]/button').click()

        # 找到搜索框，输入关键字
        self.driver.find_element_by_xpath('//input[@class="zp-search__input"]').send_keys(key)

        time.sleep(1)

        # 找到搜索按钮点击
        self.driver.find_element_by_xpath('//a[@class="zp-search__btn zp-search__btn--blue"]').click()

        time.sleep(5)
        # url = 'https://' + 'son' + '.www.zhaopin.com/'
        # self.driver.get(url)

        self.get_movie_list_data(key)

    def get_movie_list_data(self,key):

        #如果数据没加载完就等待五秒
        self.driver.implicitly_wait(5)

        # 将页面滚动到底部（注意这里必须要将页面滚动到底部,不然会获取不到数据）
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

        movie_list = self.driver.find_elements_by_xpath('//ul[@class="zp-container souheader__channel clearfix"]')
        print(movie_list)
        self.driver.save_screenshot('zhilian.png')




if __name__ == '__main__':
    dbspider = zhilianSpider()
    print('可以输入两个搜索关键字')
    for i in range(1):
        key = input('请输入第' + str(i) + '个关键字:')
        dbspider.queue.put(key)

    dbspider.start_spider(dbspider.queue.get())