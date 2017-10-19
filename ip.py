# coding=utf-8
import urllib
import urllib2
import re
import json

def target(ip):
    url='http://ip.chinaz.com/'+ip
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={"User-Agent":user_Agent}
    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req)
    content=response.read().decode('utf-8')
    results=re.findall('<span class="Whwtdhalf w15-0">(.*?)</span>.*?<span class="Whwtdhalf w15-0">(.*?)</span>.*?<span class="Whwtdhalf w15-0">(.*?)</span>.*?<span class="Whwtdhalf w50-0">(.*?)</span>',content,re.S)
    myips=re.findall(u'<p class="getlist pl10"><span>您来自：</span>(.*?) 	<span class="pl10">所在区域：</span>(.*?)<a href="http://tool.chinaz.com/contact" target="_blank" class="col-blue02 pl5">',content,re.S)
    try:
        result=u'您查询的IP  '+results[1][1]+'\n'+u'地址为:  '+results[1][3]+'\n'+u'本公众号当前所用IP'+myips[0][0]+'\n'+u'地址为:  '+myips[0][1]
    except BaseException as e:
        result=u'请输入正确格式的IP地址，不要搞事情。'
    finally:
        return result.encode('utf-8')
