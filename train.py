# coding=utf-8
import urllib
import urllib2
import re
def train(checi):
    url='http://search.huochepiao.com/chaxun/resultc.asp?txtCheCi='+checi
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={"User-Agent":user_Agent}
    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req)
    content=response.read().decode('gb2312')
    results=re.findall(u'车次.*?<td align="center" bgcolor="#ffffff">(.*?)</td>.*?运行时间.*?<td align="center" bgcolor="#ffffff">(.*?)</td>.*?<td height="18" colspan="4" align="center" bgcolor="#e2e2e2">(.*?)</td>.*?发车时间.*?<td align="center">(.*?)</td>.*?到站时间.*?<td align="center">(.*?)</td>',content,re.S)
    try:
        txt=results[0][2]+'\n'+results[0][0]+u'次'+'\n'+results[0][3]+u'开'+results[0][4]+u'到'+u'全程运行'+results[0][1]+'\n\n'
    except IndexError, e:
        txt=u'没有找到这个车次(⊙o⊙)哦，可能是临客，或者......你输错了吧还是想搞事情？'
        return txt.encode('utf-8')
    txts=re.findall('</td><td align="center"><a href="http://search.huochepiao.com/chezhan/.*?">(.*?)</a></td>.*?<td align="center">(.*?)</td><td align="center">(.*?)</td>',content,re.S)
    txt=txt+txts[0][0]+'    '+txts[0][1]+'    '+txts[0][2]+u'开'+'\n'
    n=len(txts)
    for i in range(1,n-1):
        txt=txt+txts[i][0]+'    '+txts[i][1]+u'到'+'    '+txts[i][2]+u'开'+'\n'
    txt=txt+txts[n-1][0]+'    '+txts[n-1][1]+u'到'+'    '+txts[n-1][2]
    return txt.encode('utf-8')
