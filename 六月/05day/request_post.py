# https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com/usercp/
# https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com/usercp/
from urllib import request, error, parse
import requests

url = "https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com/usercp/"

from_date = {
    'name': '18518753265',
    'password': 'ljh123456',
    'validate_code': '45823',
    'remem_pass': 'on',
    '_s_x_id': '77438df787d4e577575a795688af2121',
    'ljg_login': '1',
    'm_p_l': '1',
    'channel': '1',
    'position': '21',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.post(url=url, from_date=from_date, headers=headers)

print(response.status_code)
