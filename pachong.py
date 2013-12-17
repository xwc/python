#coding:utf-8
import urllib         
import urllib2             //python中固有的两个库
import re                  //引入正则表达式
import time                //引入时间函数的库
from random import choice#用来随机选择代理ip
iplist = ['114.32.36.229 8080','24.139.68.242 9090','119.115.136.226 80','219.150.117.116']
mds=["中国","科技","北邮","数学","语文","英语","科学"]  //建立一个列表，其中罗列一些关键字
output=open('output.txt','a')
for item in mds:      //对上述建立的列表中的元素进行遍历
    ip=choice(iplist)                 //从ip代理中选择一个ip
    timestamp = "%d" % time.time()
    gjc = urllib.quote(item)         //将上述列表中的关键词变成相应的url
    #print timestamp  
    url = "http://suggestion.baidu.com/su?wd="+gjc+"&p=3&cb=window.bdsug.sug&sid=&t=" + timestamp
    #print url
    time.sleep(2)                    //对爬虫的抓取速度进行限制
    header={
       "GET":url,
       "host":"suggestion.baidu.com",
       "Referer":"http://www.baidu.com/",
       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36",
       }                              //网页中的header包含了一系列重要的参数，包扩url，代理，等等
    proxy_handler = urllib2.ProxyHandler({'http': 'http://'+ip})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    for key in header:
        req.add_header(key,header[key])
        html=urllib2.urlopen(req).read()
        html1=re.findall("\"(.*?)\"",html)
        for item in html1:
            #print item
            output.write(item)
            output.write(" ")
        #time.sleep(5)
output.close()
print "All works have done!"  
