#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:32:08
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import urllib
import urllib2
import re
import random


def Joke():
    jokes = ''
    url = 'http://www.qiushibaike.com/'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers = {"User-Agent": user_Agent}
    req = urllib2.Request(url, headers=headers)
    webPage = urllib2.urlopen(req)
    data = webPage.read()
    content = data.decode('utf-8')
    items = re.findall(
        r'<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>', content, re.S)
    m = random.randint(0, 15)
    i = m
    while i < m+5:
        jokes = jokes+u'作者:  '+items[i][0]+'\n\n'+items[i][1]+'\n\n\n'
        i = i+1
    content = jokes.encode('utf-8')
    return content


def Duanzi():
    jokes = ''
    url = 'http://neihanshequ.com/'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers = {"User-Agent": user_Agent}
    req = urllib2.Request(url, headers=headers)
    webPage = urllib2.urlopen(req)
    data = webPage.read()
    content = data.decode('utf-8')
    items = re.findall(
        '<span class="name">(.*?)</span>.*?<div class=.*?<h1 class="title">.*?<p>(.*?)</p>.*?</h1>', content, re.S)
    m = random.randint(0, 15)
    i = m
    while i < m+5:
        jokes = jokes+u'作者:  '+items[i][0]+'\n\n'+items[i][1]+'\n\n\n'
        i = i+1
    content = jokes.encode('utf-8')
    return content


def Pic():
    jokes = ''
    url = 'http://neihanshequ.com/pic/'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers = {"User-Agent": user_Agent}
    req = urllib2.Request(url, headers=headers)
    webPage = urllib2.urlopen(req)
    data = webPage.read()
    content = data.decode('utf-8')
    items = re.findall(
        '<div class="img-wrapper">.*?data-src="(.*?)".*?data-image-info', content, re.S)
    m = random.randint(0, 15)
    i = m
    while i < m+6:
        jokes = jokes+items[i]+'\n\n'
        i = i+1
    content = jokes.encode('utf-8')
    return content


def WhuPmc():
    url = 'http://pmc.whu.edu.cn/pmcnew/'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers = {"User-Agent": user_Agent}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    content = response.read().decode('gb2312', 'ignore')
    results = re.findall(
        '<div class="h2"><a href="/list/1">.*?</a></div>(.*?)<div class="h2"><a href="/list/2">.*?</a></div>', content, re.S)
    titles = re.findall(
        '<li><a href="(.*?)" target="_self" title=\'(.*?)\'>\r\n\t(.*?)\r\n&nbsp;', results[0], re.S)
    txt = ''
    m = len(titles)
    n = 0
    while n < m:
        txt = txt+titles[n][1]+'   '+titles[n][2]+'\n\n' + \
            'http://pmc.whu.edu.cn'+titles[n][0]+'\n\n'
        n = n+1
    content = txt.encode('utf-8')
    return content


def BitSmen():
    url = 'http://smen.bit.edu.cn/'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers = {"User-Agent": user_Agent}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    content = response.read().decode('utf-8', 'ignore')
    results = re.findall(u'<h2>通知公告</h2>(.*?)<h2>新闻动态</h2>', content, re.S)
    titles = re.findall(
        '<a href="(.*?)" title="(.*?)" target="_blank">', results[0], re.S)
    dates = re.findall('<span>(.*?)</span>(.*?)</li>', results[0], re.S)
    txt = ''
    m = len(titles)
    n = 0
    while n < m:
        txt = txt+titles[n][1]+'  '+dates[n][1]+'/'+dates[n][0] + \
            '\n\n'+'http://smen.bit.edu.cn/'+titles[n][0]+'\n\n'
        n = n+1
    content = txt.encode('utf-8')
    return content
