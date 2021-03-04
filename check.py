from bs4 import BeautifulSoup
import re
import json
from pythonping import ping


class IpStatus:

    def __init__(self, ):
        self.html_data = self.__load_data()
        self.ips = set(self.__load_ips())

    @staticmethod
    def __load_data():
        with open('data/web_page.txt', 'r') as f:
            return f.readlines()

    def parse_data(self):
        pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        result = []
        for line in self.html_data:
            # print(line)
            ip = re.findall(pattern, line)
            if len(ip) > 0:
                ip = ''.join(ip)
                result.append(ip)
        return result

    @staticmethod
    def save_ips(parsed_data):
        with open('data/ips.json', 'w') as f:
            result = []
            for ip in parsed_data:
                result.append(ip)
            f.writelines(json.dumps(result))

    @staticmethod
    def __load_ips():
        with open('data/ips.json', 'r') as f:
            result = json.loads(f.read())
        return result

    def start(self, parse_data=False, save_ips=False):
        if parse_data:
            self.parse_data()
        if save_ips:
            self.save_ips()
        counter = 0
        for ip in self.ips:
            print(f"{counter}/{len(self.ips)}")
            print(f"{ip} is checking...")
            ping(ip, verbose=True)
            counter += 1
            print('*' * 20)
