import requests
import time
from random import randint
import random
from fake_useragent import UserAgent    # 伪装头
import eventlet                         # 导入 eventlet 这个模块,用于跳出代码超时问题

ua = UserAgent()  # 获取伪装头
proxy_list = ['221.122.91.74:9401', '221.122.91.60:80', '58.220.95.90:9401', '58.220.95.86:9401', '221.122.91.61:80',
              '58.220.95.116:10122', '58.220.95.42:10174', '220.174.236.211:8091', '221.122.91.74:9401',
              '221.122.91.60:80', '58.220.95.90:9401', '58.220.95.86:9401', '221.122.91.61:80', '58.220.95.116:10122',
              '58.220.95.42:10174', '116.196.85.150:3128', '221.122.91.76:9480', '218.59.139.238:80',
              '144.217.101.245:3129', '103.115.14.158:80', '103.115.14.41:80', '180.250.12.10:80',
              '198.50.163.192:3129', '96.113.165.182:3128', '58.220.95.54:9400', '221.122.91.65:80',
              '51.75.147.41:3128', '103.115.14.43:80', '118.174.232.239:39258', '78.47.16.54:80',
              ]

user_agent = str(ua.random)             # 随机获取伪装头
headers = {'User-Agent': user_agent}
proxy_ip = random.choice(proxy_list)    # 随机获取代理IP
proxies = {'http': 'http://' + proxy_ip}
print('代理ip:{}'.format(proxy_ip))
req = requests.get('http://icanhazip.com/', headers=headers, proxies=proxies)
print('识别ip：{}'.format(req.content))