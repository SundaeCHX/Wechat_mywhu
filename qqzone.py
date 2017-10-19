#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:32:08
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import urllib
import urllib2
import json
import sys
import re


def Send(m):
    reload(sys)
    sys.setdefaultencoding("utf8")
    url = 'http://h5.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?g_tk=763847912'
    data = urllib.urlencode({'qzreferrer': r'http%3A%2F%2Fuser.qzone.qq.com%2F**********', 'syn_tweet_verson': '1',
                             'paramstr': '1', 'pic_template': '', 'richtype': '', 'richval': '', 'special_url': '', 'subrichtype': '', 'who': '1',
                             'con': m+'\n'+u'————来自微信公众平台【在路上随风走】', 'feedversion': '1', 'ver': '1', 'ugc_right': '1', 'to_sign': '0',
                             'hostuin': '1657723960', 'code_version': '1', 'format': 'fs'})
    cookie = 'pgv_pvi=2209861632; pt2gguin=o1657723960; RK=zue+Nb+WNv; ptcz=1201d762fe5e5900cd96b36b75a9ba5cac403e7f7d3925c315e4a0d13eda2999; pgv_pvid=4243429905; o_cookie=1657723960; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=14; pgv_info=ssid=s7984145305; uin=o1657723960; skey=@TJ85yDLYf; ptisp=ctc; p_uin=o1657723960; p_skey=I3wEETJfQoPkZbBnYVoKrw7rgOewsNiNL1lMiNxW*8Y_; pt4_token=V48OsiS4DNF9dd1vTWGbS8SDwppfj1n655wUshEysy8_; fnc=2; blabla=dynamic; Loading=Yes'
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    referer = 'http://user.qzone.qq.com/**********'
    headers = {"Cookie": cookie, "User-Agent": user_Agent, "Referer": referer}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req, data.encode('utf-8'))
    content = response.read().decode('utf-8')
    results = re.findall(
        '{"code":-3000,"message":"(.*?)","needVerify":0,"subcode":-4001}', content, re.S)
    if results == []:
        return 'Send Success'
    else:
        return 'Cookies Failed'
