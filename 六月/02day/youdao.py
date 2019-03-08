from urllib import request, parse
import json

key = input('输入要翻译的关键字:')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

form_data = {
    'i': key,
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

b_form_data = parse.urlencode(form_data).encode('utf-8')

req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
req = request.Request(url, data=b_form_data, headers=req_header)

response = request.urlopen(req)

if response.status == 200:
    print('成功')
    # print(response.read().decode('utf-8'))
    data = json.loads(response.read().decode('utf-8'))
    print(type(data))
    print(data)
    result = data['translateResult'][0][0]['tgt']
    print(result)
