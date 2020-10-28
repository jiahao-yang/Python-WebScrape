import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_univ_list(ulist, soup):
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def find_province(ulist, soup, province):
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            if tds[2].string.strip() == province:
                ulist.append([tds[0].string, tds[1].string, tds[2].string])


def print_univ_list(ulist, num):
    print("{:^10}\t\t{:^6}\t\t{:^10}".format("Rank", "University", "Province/City"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t\t{:^6}\t\t{:^10}".format(u[0].strip(), u[1].strip(), u[2].strip()))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'
    html = get_html_text(url)
    soup = BeautifulSoup(html, "html.parser")
    fill_univ_list(uinfo, soup)
    print_univ_list(uinfo, 20)

    print("\n")

    u_province_list = []
    province = "广东"
    print("===== Universities in {} =====".format(province))
    find_province(u_province_list, soup, province)
    print_univ_list(u_province_list, 20)


main()
