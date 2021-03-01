from bs4 import BeautifulSoup
import re
import json


def load_data():
    with open('data/web_page.txt', 'r') as f:
        return f.readlines()



def parse_data(html_doc):
    pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    result = []
    
    for line in html_doc:
        # print(line)
        ip = re.findall(pattern, line)
        if len(ip) > 0:
            ip = ''.join(ip)
            result.append(ip)

    return result


def save_data(parsed_data):
    with open('data/ips.json', 'w') as f:
        result = []
        for ip in parsed_data:
            result.append(ip)
        f.writelines(json.dumps(result))

def load_ips():
    with open('data/ips.json', 'r') as f:
        result = json.loads(f.read())
    return result

