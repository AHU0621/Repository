
import requests
import time

import eventlet

# url = "http://tougao.12371.cn/gaojian.php?tid=3761117" #选调生萌新的基层“山海情”
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
# headers = {'User-Agent': user_agent}
# proxy_ip = '58.220.95.32:10174'
# proxies={'http': 'http://' + proxy_ip}
#
#
# response = requests.get(url, headers=headers,proxies=proxies)
# print(response)

eventlet.monkey_patch(time=True)    # 必须加这条代码
with eventlet.Timeout(2, False):  # 设置超时时间为100秒
    time.sleep(2.1)
    print("开始执行请求:\t", end='')
print('超时')