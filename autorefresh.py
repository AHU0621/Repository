# 用于刷网页的访问量（嘘……）
#   代理IP列表容易失效，可以运行一次IP.py重新获取IP列表
#   可增加成功率计算，剩余运行时间估算


import requests
import time
from random import randint
import random
from fake_useragent import UserAgent    # 伪装头
import eventlet                         # 导入 eventlet 这个模块,用于跳出代码超时问题

url_list = [
            # "http://tougao.12371.cn/gaojian.php?tid=3761117",   # 选调生萌新的基层“山海情”
            # "http://tougao.12371.cn/gaojian.php?tid=3761117", # 选调生萌新的基层“山海情”
            # "http://tougao.12371.cn/gaojian.php?tid=3761117", # 选调生萌新的基层“山海情”
            # "http://tougao.12371.cn/gaojian.php?tid=3784973",   # 治基层“三病”安民众之心
            # "http://tougao.12371.cn/gaojian.php?tid=3777755", # 修炼“志、魂、胆” 反腐倡廉一直在路上
            # "http://tougao.12371.cn/gaojian.php?tid=3777755",
            # "http://tougao.12371.cn/gaojian.php?tid=3789574",   # 以“每日三省”提“政治三力”
            # "http://tougao.12371.cn/gaojian.php?tid=3795495",   # @党员 权利的正确行使方式
            # "http://tougao.12371.cn/gaojian.php?tid=3807351",   # 用党史“活水”滋润发展“根须”
            "http://tougao.12371.cn/gaojian.php?tid=3821673", # 让脱贫攻坚的“阳光”照亮乡村振兴的征程
            ]

times = 250   # 需要的次数

# ua = UserAgent(path=r'F:\Program Files\Python脚本\autorefresh\ua.json')   # 本地获取
ua = UserAgent()  # 网络获取伪装头
proxy_list = ['221.122.91.74:9401', '221.122.91.60:80', '58.220.95.90:9401', '58.220.95.86:9401', '221.122.91.61:80',
              '58.220.95.116:10122', '58.220.95.42:10174', '220.174.236.211:8091', '221.122.91.74:9401',
              '221.122.91.60:80', '58.220.95.90:9401', '58.220.95.86:9401', '221.122.91.61:80', '58.220.95.116:10122',
              '58.220.95.42:10174', '116.196.85.150:3128', '221.122.91.76:9480', '218.59.139.238:80',
              '144.217.101.245:3129', '103.115.14.158:80', '103.115.14.41:80', '180.250.12.10:80',
              '198.50.163.192:3129', '96.113.165.182:3128', '58.220.95.54:9400', '221.122.91.65:80',
              '51.75.147.41:3128', '103.115.14.43:80', '118.174.232.239:39258', '78.47.16.54:80',
              '104.248.123.76:18080', '136.233.215.139:80', '208.138.24.254:80',
              '5.196.23.219:80', '49.204.79.81:80', '159.65.171.69:80', '136.243.254.196:80',
              '162.214.92.202:80', '94.23.91.209:80', '203.198.94.132:80', '104.248.123.76:18080',
              '136.233.215.137:80', '218.59.139.238:80', '136.233.215.139:80', '39.106.223.134:80',
              '203.198.94.132:80', '221.122.91.61:80', '221.122.91.65:80', '221.182.31.54:8080',
              '162.214.92.202:80', '203.198.94.132:80', '104.248.123.76:18080', '122.226.57.70:8888',
              '136.233.215.139:80', '5.196.23.219:80', '208.138.24.254:80', '159.65.171.69:80',
              '220.174.236.211:8091', '221.122.91.59:80', '218.59.139.238:80', '161.35.4.201:80',
              '181.129.183.19:53281',
              ]

# ↑可以通过IP.py重新获取代理IP列表

num = 0       # 记录总运行次数
count = 0     # 记录成功次数
response = 0  # response初值，防止首次刷新异常而未定义response中断程序

while count < times:
    num = num + 1
    print(time.strftime('\n\n%Y.%m.%d %H:%M:%S', time.localtime(time.time())), end='')
    # noinspection PyBroadException
    eventlet.monkey_patch(time=True)    # 必须加这条代码
    try:  # 正常运行
        with eventlet.Timeout(20, False):  # 设置超时时间为20秒
            print("\t第 {} 次运行,".format(num) + '已成功 ' + str(count) + " 次")
            user_agent = str(ua.random)  # 获取随机伪装头
            headers = {'User-Agent': user_agent}
            proxy_ip = random.choice(proxy_list)  # 随机获取代理IP
            proxies = {'http': 'http://' + proxy_ip}  # http类型访问，如果不确定访问类型，可以将http和https都放进去

            url = random.choice(url_list)
            print('当前执行url: %s' % url)
            print('当前代理user_agent：%s' % user_agent)
            print('当前代理ip：%s' % proxy_ip)
            print("开始执行请求:\t", end='')
            response = requests.get(url, headers=headers, proxies=proxies)

            # req = requests.get('http://icanhazip.com/', headers=headers, proxies=proxies)
            # print('识别ip：{}'.format(req.content))
            # ↑用于检查代理IP设置是否有效，访问此url会返回当前IP地址↑
            # print('{}'.format(response.content))

            # print(str(response)+"\t未超时")
            # 超时跳出后仍然会执行下面的语句，如果上一次响应码为200则会导致计数不准
            if response.status_code == 200:
                a = randint(1, 3)
                count = count + 1
                print('↑运行成功！已成功 ' + str(count) + ' 次,'+"等待{}秒后继续执行↓".format(a), end='')
                rate = (count / num) * 100
                print("\t当前成功率:\t{:.1f}%".format(rate))
                time.sleep(a)

    except Exception:   # 异常
        # except:  # 异常
        print("\t运行异常" + str(response), end='')   # 存在执行请求前出现异常而响应码未更新的情况(仍为200)
        # 若出现打印出的响应码为200的情况，可以使用当前代理再次执行error_test.py从而判断是否为代理IP问题，删除后可以提高成功率
        rate = (count / num) * 100
        print("\t当前成功率:\t{:.1f}%".format(rate))
        for i in range(randint(1, 3), 0, -1):
            print("\r刷新失败，等待{}秒后再次尝试".format(i), end='')
            time.sleep(1)
print("\n\t运行结束!总共运行了" + str(num) + "次,其中成功{}次".format(count))
