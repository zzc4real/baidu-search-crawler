# -*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
import pandas as pd
import numpy

reload(sys)
sys.setdefaultencoding("utf-8")

def getfromBaidu(word, page_num):
    clist = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'

    for k in range(1, page_num):
        print(url)
    path = etree.HTML(requests.get(url, headers).content)
    flag = 11
    if k == 1:
        flag = 10
    for i in range(1, flag):
        x = []
    title = ""
    time = ""
    link = ""
    # # executing title
    for j in path.xpath('//*[@id="%d"]/h3/a//text()' % ((k - 1) * 10 + i)):
        title += j
    # print (title)
    x.append(title)
    }
    baiduurl = 'http://www.baidu.com'
    url = 'http://www.baidu.com.cn/s?wd=' + word + '&pn=0'
    html = requests.get(url=url,headers=headers)
    path = etree.HTML(html.content)

    #用k来控制爬取的页码范围

            # executing time
            for m in  path.xpath('//*[@id="%d"]//div[@class="c-abstract"]//span[@class=" newTimeFactor_before_abs m"]//text()'%((k-1)*10+i)):
                m = m[:-3]
                time += m
            # print (time)
            x.append(time)

            # executing link
            for l in path.xpath('//*[@id="%d"]//div[@class="f13"]//a[@class="c-showurl"]/@href'%((k-1)*10+i)):
                link += l
            # print (link)
            x.append(link)

            clist.append(x)
        url = 'http://www.baidu.com.cn/s?wd=' + word + '&pn=' + str(k*10)

    data = pd.DataFrame(clist)
    data.to_csv('./a.csv', index=False, header=False, encoding="utf_8_sig")
    # print(clist)

#主程序测试函数
if __name__ == '__main__':
    getfromBaidu('Tolarno Galleries',6)