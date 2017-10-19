#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:32:08
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import time


class Msg(object):

    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):

    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)


class FormatMsg(Msg):

    def __init__(self, toUserName, fromUserName, media_id):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = media_id

    def send(self):
        XmlForm = """
        <xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[voice]]></MsgType>
		<Voice>
		<MediaId><![CDATA[{MediaId}]]></MediaId>
		</Voice>
		</xml>
		"""
        return XmlForm.format(**self.__dict)


class ImageMsg(Msg):

    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)


class FmMsg(Msg):

    def __init__(self, toUserName, fromUserName):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>6</ArticleCount>
		<Articles>
		<item>
		<Title><![CDATA[蜻蜓FM]]></Title>
        <PicUrl><![CDATA[http://upload.ikanchai.com/2015/1113/1447406591258.JPG]]></PicUrl>
		<Url><![CDATA[http://qingting.fm/]]></Url>
		</item>
		<item>
		<Title><![CDATA[喜马拉雅FM]]></Title>
        <PicUrl><![CDATA[http://fdfs.xmcdn.com/group10/M0B/79/37/wKgDZ1YI5L6yuiw3AAMmKmCoXpU967.jpg]]></PicUrl>
		<Url><![CDATA[http://www.ximalaya.com/explore/]]></Url>
		</item>
        <item>
		<Title><![CDATA[CNR中国之声]]></Title>
        <PicUrl><![CDATA[http://www.radio.cn/templates/default/images/ttx_bg.jpg]]></PicUrl>
		<Url><![CDATA[http://www.radio.cn/index.php?option=default,index_baidu&c=3]]></Url>
		</item>
        <item>
		<Title><![CDATA[CNR音乐之声]]></Title>
        <PicUrl><![CDATA[http://fdfs.xmcdn.com/group13/M01/50/00/wKgDXVcbLGHy5L5aAAG3XT4-TSc418.jpg]]></PicUrl>
		<Url><![CDATA[http://qingting.fm/channels/388]]></Url>
		</item>
        <item>
		<Title><![CDATA[上海KFM981]]></Title>
        <PicUrl><![CDATA[http://s1.qingting.fm/images/player/1.jpg]]></PicUrl>
		<Url><![CDATA[http://qingting.fm:8000/channels/5022023]]></Url>
		</item>
        <item>
		<Title><![CDATA[AsiaFM亚洲音乐台]]></Title>
        <PicUrl><![CDATA[http://img8.cyzone.cn/uploadfile/2014/1118/20141118082658827.jpg]]></PicUrl>
		<Url><![CDATA[http://qingting.fm:8000/channels/4581]]></Url>
		</item>
		</Articles>
		</xml>
        """
        return XmlForm.format(**self.__dict)


class QrMsg(Msg):

    def __init__(self, toUserName, fromUserName, url, qrurl):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Url'] = url
        self.__dict['QrUrl'] = qrurl

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>1</ArticleCount>
		<Articles>
		<item>
		<Title><![CDATA[二维码已生成，点击查看]]></Title>
        <PicUrl><![CDATA[{Url}]]></PicUrl>
		<Url><![CDATA[{QrUrl}]]></Url>
		</item>
		</Articles>
		</xml>
        """
        return XmlForm.format(**self.__dict)
