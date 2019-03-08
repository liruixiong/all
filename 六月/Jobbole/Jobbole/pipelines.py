# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json, pymysql


# 管道文件，过滤数据和持久化
class JobbolePipeline(object):

    def __init__(self):
        self.file = open('jobbole.json', 'a+')

    def process_item(self, item, spider):
        """
        :param item: item：这个就是爬虫文件中yield 过来的item (是一个对象)
        :param spider: 是一个对象，爬虫文件实例化的对象（JobboleSpider）
        :return:
        """
        # 这个方法是必须要实现的，
        print('1111经过了管道')
        # 先将item转为字典
        data = dict(item)
        json_data = json.dumps(data, ensure_ascii=False)
        self.file.write(json_data + '\n')

        # 注意假如有多个管道，只有return item 之后，
        # 下一个管道此案呢个接收到item
        return item

    def open_spider(self, spider):
        """
        并不是必须要实现的方法，在爬虫运行的时候，执行一次
        :param spider:
        :return:
        """
        print('爬虫开始运行')

    def close_spider(self, spider):
        """
        并不是必须要实现的方法，在爬虫结束的时候，执行一次
        :param spider:
        :return:
        """
        self.file.close()


class JobbolePipelineDb(object):
    def __init__(self):
        self.mysql_con = pymysql.Connect(
            '127.0.0.1', 'root', '123',
            'bole', 3306, charset='utf8'
        )

        self.cursor = self.mysql_con.cursor()

    def open_spider(self,spider):
        
        print('爬虫开始')

    def close_spider(self,spider):

        self.mysql_con.close()

    def process_item(self, item, spider):
        print('2222经过了管道')
        data = dict(item)
        insert_sql = """
            INSERT INTO bole(%s)
            VALUES(%s)
            """ % (','.join(data.keys()), ','.join(['%s'] * len(data)))

        try:
            self.cursor.execute(insert_sql, list(data.values()))
            self.mysql_con.commit()
            print('数据插入成功')
        except Exception as err:
            print(err)
            self.mysql_con.rollback()
        return item
    def close_spider(self,spder):
        self.cursor.close()
        self.mysql_con.close()