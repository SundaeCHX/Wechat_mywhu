#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:32:08
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'event':
        return EventMsg(xmlData)
    if msg_type == 'text':
        return TextMsg(xmlData)
    if msg_type == 'voice':
        return FormatMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)


class Msg(object):

    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text


class EventMsg(Msg):

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Event = xmlData.find('Event').text.encode("utf-8")


class TextMsg(Msg):

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")


class ImageMsg(Msg):

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text


class FormatMsg(Msg):

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.media_id = xmlData.find('MediaId').text
        self.Recognition = xmlData.find('Recognition').text.encode("utf-8")
        self.Format = xmlData.find('Format').text
