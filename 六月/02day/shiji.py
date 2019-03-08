from urllib import request, parse
import json
import ssl

url = "http://search.jiayuan.com/v2/search_v2.php"

form_data = {
    "sex": "f",
    "key": "",
    "stc": "1:33,2:20.28,23:1",
    "sn": "default",
    "sv": "1",
    "p": "1 ",
    "f": "search",
    "listStyle": " bigPhoto",
    "pri_uid": "0",
    "jsversion": "v5",
}

h_data = parse.urlencode(form_data).encode("utf-8")

req_header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

req = request.Request(url, data=h_data, headers=req_header)
response = request.urlopen(req)

# print(response.status)
# print(response.url)
ser = response.read().decode("utf-8")
ser1 = ser.replace("##jiayser##", "")
ser2 = ser1.replace("//", "")
result_data = json.loads(ser2)
print(result_data)

positiones1 = result_data['userInfo']

for position in positiones1:
    jobInfo = {}
    jobInfo['nickname'] = position['nickname']
    jobInfo['sex'] = position['sex']
    jobInfo['realUid'] = position['realUid']
    jobInfo['work_location'] = position['work_location']
    jobInfo['image'] = position['image']
    jobInfo['shortnote'] = position['shortnote']
    jobInfo['marriage'] = position['marriage']
    jobInfo['age'] = position['age']
    jobInfo['randTag'] = ';'.join(position['randTag'].replace('<span>', '').split('</span>'))

    print(jobInfo)
    # with open('世纪佳缘.json', 'a+') as file:
    #     data = json.dumps(jobInfo, ensure_ascii=False)
    #     file.write(data + '\n')

