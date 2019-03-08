from urllib import request
from urllib import parse

url = 'http://fanyi.youdao.com/'

headers = {
    'User_Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
formdata = {
    'i': '你好',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}
data = parse.urlencode(formdata).encode('utf-8')
req = request.Request(url, data=data, headers=headers)
response = request.urlopen(req)
print(response.read().decode('utf-8'))
