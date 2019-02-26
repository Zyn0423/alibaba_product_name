import requests
import re
from lxml import etree

def gethtml(urls):
    try:
        headers = {
            "cookie": "",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
        html = requests.get(urls, headers=headers, timeout=30)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        print(html.status_code)
        return html.text
    except:
        print('获取失败')
# 解析
def html_list(list_, HTml):
    try:
        price = re.findall(r'\"view_price\"\:\"[\d\.]*\"', HTml)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', HTml)
        # xpth 的匹配 "//*[@class='row row-2 title']/a/text()[2]"
        for i in range(len(price)):
            price_data = eval(price[i].split(':')[1])
            tlt_data = eval(tlt[i].split(':')[1])
            list_.append([price_data, tlt_data])
    except:
        print('解析抛出异常')
# 展示输出
def print_list(list_):
    show_ = "{:3}\t{:10}\t{:10}"
    print(show_.format('序号', '价格', '品牌'), chr(12288))
    count = 0
    for i in list_:
        count += 1
        print(show_.format(count, i[0], i[1]), chr(12288))


# 主函数
def mian():
    url = 'https://s.taobao.com/search?q='
    params = '汤姆福特80'
    list_ = []
    for i in range(3):
        # 拼接url
        urls = url + params + '&s=' + str(i * 44)
        HTml = gethtml(urls)
        html_list(list_, HTml)
    print_list(list_)


mian()
