#获取有效代理IP列表

import requests
from lxml import etree
import time
from fake_useragent import UserAgent


class XiLaIp_Spider:

    def __init__(self):
        self.url = 'http://www.xiladaili.com/gaoni/'
        ua = UserAgent()
        user_agent = str(ua.random)
        self.headers = {
            'User-Agent': user_agent,
            #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'cookie': 'td_cookie=1539882751; csrftoken=lymOXQp49maLMeKXS1byEMMmsavQPtOCOUwy6WIbfMNazZW80xKKA8RW2Zuo6ssy; Hm_lvt_31dfac66a938040b9bf68ee2294f9fa9=1592547159; Hm_lvt_9bfa8deaeafc6083c5e4683d7892f23d=1592535959,1592539254,1592612217; Hm_lpvt_9bfa8deaeafc6083c5e4683d7892f23d=1592612332',
        }
        self.proxy = '116.196.85.150:3128'
        self.proxies = {
            "http": "http://%(proxy)s/" % {'proxy': self.proxy},
            "https": "http://%(proxy)s/" % {'proxy': self.proxy}
        }
        self.list1 = []

    def get_url(self):
        file = open('Ip_Proxy.txt', 'a', encoding='utf-8')
        ok_file = open('OkIp_Proxy.txt', 'a', encoding='utf-8')
        print("开始尝试获取IP列表，请耐心等待！")
        for index in range(50):
            time.sleep(1)
            try:
                print("*",end='')
                # res = requests.get(url=self.url if index == 0 else self.url + str(index) + "/", headers=self.headers,
                                   # proxies=self.proxies, timeout=10).text
                res = requests.get(url=self.url if index == 0 else self.url + str(index) + "/", headers=self.headers,
                                timeout=10).text
            except:
                continue
            data = etree.HTML(res).xpath("//*[@class='mt-0 mb-2 table-responsive']/table/tbody/tr/td[1]")
            # '//*[@id="scroll"]/table/tbody/tr/td[1]'
            score_data = etree.HTML(res).xpath("//*[@class='mt-0 mb-2 table-responsive']/table/tbody/tr/td[8]")
            for i, j in zip(data, score_data):
                # file.write(i.text + '\n')
                score = int(j.text)
                # 追加评分率大于十万的ip
                if score > 50000:
                    self.list1.append(i.text)
            set(self.list1)
        file.close()
        print("\n")
        print(self.list1)

        ok_ip = []
        print("验证代理ip是否有效，请耐心等待！")
        for i in self.list1:
            print("*", end='')
            try:
                # 验证代理ip是否有效
                res = requests.get(url='http://tougao.12371.cn/gaojian.php?tid=3789574', headers=self.headers, proxies={'http': 'http://' + i},
                                   timeout=5)

                if res.status_code == 200:
                    # ok_file.write(i + '\n')
                    ok_ip.append(i)
            except:
                continue
        ok_file.close()
        print("*********")
        print(ok_ip)
        return ok_ip

    def run(self):
        return self.get_url()


dl = XiLaIp_Spider()
dl.run()