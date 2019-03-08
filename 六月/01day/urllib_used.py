from urllib import request
from urllib import parse
import os

parmas = ['李白', '杜甫']
for i in parmas:
    parmas = {'wd': i}
    parmas = parse.urlencode(parmas)

    for j in range(0, 10):
        x = j * 10
        c = {'&pn': x}
        c = parse.urlencode(c)
        c = parse.unquote(c)
        url = 'https://www.baidu.com/s?' + parmas + c

        req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

        req = request.Request(url=url, headers=req_headers)
        response = request.urlopen(req, timeout=20)
        html = response.read().decode('utf-8')
        print(len(html))
        # os.makedirs(i)
        print(response.status)
        print(response.url)
