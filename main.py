from pythonping import ping
# from ips import ip_list
from crawler import load_data, save_data, parse_data, load_ips




if __name__ == "__main__":
    # html_doc = load_data()
    # parsed_data = parse_data(html_doc)
    # save_data(parsed_data)

    ip_list = load_ips()

    counter = 1
    for ip in ip_list:
        print(f"{counter}/{len(ip_list)}")
        print(f"{ip} is checking...")
        ping(ip, verbose=True)
        counter += 1
        print('*'*20)