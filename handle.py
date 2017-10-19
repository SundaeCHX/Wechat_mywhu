#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:28:25
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import hashlib
import reply
import receive
import web
import robot
import joke
import smtp
import train
import ip
import qqzone
import morse
import free
from sinastorage.bucket import SCSBucket
import sinastorage


class Handle(object):

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'event':
                    event = recMsg.Event
                    if event == 'subscribe':
                        replyMsg = reply.TextMsg(
                            toUser, fromUser, '欢迎订阅【在路上随风走】，回复“功能介绍”可查看功能简介噢，对了，在这还可以和机器人语音聊天呢，更多精彩就等你自己探索啦！')
                        return replyMsg.send()
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    if content == '电台' or content == 'fm' or content == 'Fm' or content == 'FM':
                        replyMsg = reply.FmMsg(toUser, fromUser)
                        return replyMsg.send()
                    if content == '糗百' or content == '糗事百科' or content == '臭事百科' or content == '丑事百科':
                        word = joke.Joke()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '段子' or content == '内涵段子' or content == '内涵段子手':
                        word = joke.Duanzi()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '搞笑图片' or content == '内涵图片' or content == '内涵图':
                        word = joke.Pic()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '成绩单' or content == '成绩' or content == '查成绩' or content == '成绩查询':
                        word = '把链接复制到浏览器中查询速度更快(⊙o⊙)哦'+'\n' + \
                            'http://sundae.applinzi.com/signin'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '动机院公告' or content == '动机院' or content == '武大动机' or content == '动力与机械学院':
                        word = joke.WhuPmc()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '机电学院' or content == '北理机电' or content == '机电学院公告':
                        word = joke.BitSmen()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:4] == 'send' or content[0:4] == 'Send':
                        txt = content[5:-1]+content[-1]
                        word = qqzone.Send(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:5] == 'train' or content[0:5] == 'Train':
                        txt = content[6:-1]+content[-1]
                        word = train.train(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:5] == 'morse' or content[0:5] == 'Morse' or content[0:5] == 'MORSE':
                        txt = content[6:-1]+content[-1]
                        word = morse.morse(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:2] == 'm0' or content[0:2] == 'M0':
                        txt = content[3:-1]+content[-1]
                        word = morse.morse(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:6] == 'umorse' or content[0:6] == 'Umorse' or content[0:6] == 'UMORSE':
                        txt = content[7:-1]+content[-1]
                        word = morse.umorse(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:3] == 'um0' or content[0:3] == 'Um0' or content[0:2] == 'UM0':
                        txt = content[4:-1]+content[-1]
                        word = morse.umorse(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:2] == 'm1' or content[0:2] == 'M1':
                        txt = content[3:-1]+content[-1]
                        word = morse.morse1(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:3] == 'um1' or content[0:3] == 'UM1':
                        txt = content[4:-1]+content[-1]
                        word = morse.umorse1(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:2] == 'ip' or content[0:2] == 'Ip' or content[0:2] == 'IP':
                        txt = content[3:-1]+content[-1]
                        word = ip.target(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:2] == 'hp' or content[0:2] == 'Hp' or content[0:2] == 'HP':
                        txt = content[3:-1]+content[-1]
                        word = free.freestyle(txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '余额' or content == '校园卡余额':
                        word = '把链接复制到浏览器中查询速度更快(⊙o⊙)哦'+'\n' + \
                            'http://sundae.applinzi.com/signin'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '关机':
                        word = smtp.smtp()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '监控' or content == '远程监控':
                        word = smtp.control()
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == 'html' or content == '源代码':
                        word = '欢迎使用网页源代码查询功能'+'\n'+'http://sundae.applinzi.com/html'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '主页' or content == 'Sundae' or content == '网站' or content == 'sundae':
                        word = '欢迎访问 Sundae『在路上随风走』个人网站'+'\n'+'http://sundae.applinzi.com/home'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '博客':
                        word = '欢迎访问 Sundae『在路上随风走』个人博客'+'\n'+'http://sundae.applinzi.com/blog'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == '骑行日记':
                        word = '欢迎访问 Sundae『在路上随风走』个人博客——骑行日记'+'\n'+'http://sundae.applinzi.com/diary'
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content[0:2] == 'QR' or content[0:2] == 'qr' or content[0:2] == 'Qr':
                        txt = content[3:-1]+content[-1]
                        sinastorage.setDefaultAppInfo(
                            'w5il63SKTaSzZlCvuy8l', 'ae6523ffe7531606e34a6285fd3554f9203e2a2e')
                        s = SCSBucket('sundae')
                        url = s.make_url_authed('picture/whubj.jpg')
                        qrurl = 'http://qr.topscan.com/api.php?text='+txt
                        replyMsg = reply.QrMsg(toUser, fromUser, url, qrurl)
                        return replyMsg.send()
                    if content == '功能介绍' or content == '功能' or content == '功能简介':
                        word = '''
功能简介：
1.聊天机器人，支持文字聊天和语音聊天。
2.电台，收听电台，关键字：电台。
3.成绩查询，查询所有成绩，关键字：成绩查询、成绩单等。
4.糗事百科，后台爬虫爬取糗百官网最新最热段子，关键字：糗百等。
5.内涵段子，后台爬虫爬取内涵段子官网最新段子，关键字：段子。
6.搞笑图片，后台爬虫爬取内涵段子官网内涵图，关键字：内涵图、搞笑图片等。
7.武汉大学动机院公告，爬取了官网抓了同步更新的公告，关键字：动机院等。
8.北京理工大学机电学院公告，爬取了官网同步更新的公告，关键字：机电学院等。
9.网站，我的个人网站，关键字：网站等。
10.博客，我的个人博客，关键字：博客等。
11.网页源代码，在手机上也可以查看指定网站的源代码，关键字：源代码等。
12.Python，介绍Python语言，毕竟我后台就是用Python写的，关键字：Python。
13.火车车次，输入“train 车次”直接查询列车时刻表，关键字：Train 车次。
14.二维码，输入“QR 文字”可将文字转变为二维码，关键字：Qr、QR等。
15.摩斯密码，可以进行摩斯密码加解密，关键字：Morse、Umorse、m1、um1等。
16.IP地址，输入“ip xx.xx.xx.xx”可以查询指定IP的地址，关键字：IP、ip等。
17.有freestyle吗，输入“hp 词语”可查询相关的押韵词语，关键字：hp、Hp等。
                        
所有关键字都支持模糊匹配，比如动机院公告、武大动机、动机院等都是同一个关键字。
                        
剩下的都是我的个人功能就不告诉大家了哈~~~
                        '''
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    if content == 'import this' or content == '后台' or content == 'Python' or content == 'python':
                        word = '''
The Zen of Python, by Tim Peters
                        
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
                        '''
                        replyMsg = reply.TextMsg(toUser, fromUser, word)
                        return replyMsg.send()
                    word = robot.Robot(content, toUser)
                    replyMsg = reply.TextMsg(toUser, fromUser, word)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                if recMsg.MsgType == 'voice':
                    content = recMsg.Recognition
                    word = robot.Robot(content, toUser)
                    replyMsg = reply.TextMsg(toUser, fromUser, word)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "Wait..."
                return 'success'
        except Exception, Argument:
            return Argument
