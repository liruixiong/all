# #使用scrapy创建项目
# scrapy startproject 项目名称
#
# #创建爬虫文件
# #进入项目下的spiders文件夹下
# start genspider 爬虫文件名称(不能跟项目名称重复) 网站的域
#
# 运行爬虫文9件
# scrapy crawl 爬虫名称


#项目的目录结构
# spiders文件夹 -> 所有的爬虫文件都放在这个文件夹下
#     爬虫文件：
#         name :爬虫文件的名称
#         allow_domains ：设置允许爬取网站的相对域
#         start_urls：设置起始url
#         def parse（self，response）：
#             回调函数，获取请求（request）的响应结果
#
# items.py 定制要爬取的字段，爬虫文件中获取的数据需要赋值给这里的实例化对象
#
# pipeline ：数据管道
#     管道文件
#     （注意：管道文件能够接受到item有两个前提
#         1.确保爬虫文件中获取的item yield 给管道
#         2.确保管道文件设置文件中激活
