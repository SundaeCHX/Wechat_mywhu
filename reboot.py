#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:32:08
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import urllib
import urllib2
import re


def Robot(content, toUser):
    api = 'http://www.tuling123.com/openapi/api'
    apikey = '74a91f55185f4ece8c4f89813c9fd835'
    data = urllib.urlencode({'key': apikey, 'info': content, 'userid': toUser})
    request = urllib2.Request(api, data)
    response = urllib2.urlopen(request)
    answer = response.read()
    results = re.findall('"text":"(.*?)"', answer)
    for result in results:
        return result
