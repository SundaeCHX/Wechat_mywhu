# coding=utf-8
import requests
import sys

def freestyle(msg):
    word=''
    free=msg
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    url='http://lab.crossincode.com/rhyme/get?word='+free
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={'user-agent':user_Agent}
    req=requests.get(url,headers=headers)
    content=req.json()
    for i in range(0,24):
        word=word+content[free.decode('utf-8')][i][0]+'  '
    return word.encode('utf-8')
