# coding=utf-8
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def smtp():
    from_addr='nba_soccer@163.com'
    smtp='Soccer123'
    to_addr='chxhyfx@163.com'
    smtp_sever='smtp.163.com'
    msg=MIMEMultipart()
    name1,addr1=parseaddr('Sundae <%s>' % from_addr)
    msg['From']=formataddr((Header(name1,'utf-8').encode(),addr1))
    name2,addr2=parseaddr('Administer <%s>' % to_addr)
    msg['To']=formataddr((Header(name2,'utf-8').encode(),addr2))
    msg['Subject']=Header('Shut down','utf-8').encode()
    msg.attach(MIMEText('Hello, guy...','plain','utf-8'))
    sever=smtplib.SMTP(smtp_sever,25)
    sever.set_debuglevel(1)
    sever.login(from_addr,smtp)
    sever.sendmail(from_addr,[to_addr],msg.as_string())
    sever.quit()
    return '远程控制关机成功!'

def control():
    from_addr='nba_soccer@163.com'
    smtp='Soccer123'
    to_addr='chxhyfx@163.com'
    smtp_sever='smtp.163.com'
    msg=MIMEMultipart()
    name1,addr1=parseaddr('Sundae <%s>' % from_addr)
    msg['From']=formataddr((Header(name1,'utf-8').encode(),addr1))
    name2,addr2=parseaddr('Administer <%s>' % to_addr)
    msg['To']=formataddr((Header(name2,'utf-8').encode(),addr2))
    msg['Subject']=Header('Supervisory control','utf-8').encode()
    msg.attach(MIMEText('Hello, guy...','plain','utf-8'))
    sever=smtplib.SMTP(smtp_sever,25)
    sever.set_debuglevel(1)
    sever.login(from_addr,smtp)
    sever.sendmail(from_addr,[to_addr],msg.as_string())
    sever.quit()
    return '远程监控启动，请前往QQ监视'
