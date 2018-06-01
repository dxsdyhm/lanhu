# coding:utf-8
phone={u'墨香':'13128756863',u'神秘圆圆酱':'17665310095',u'学无止境':'15270628776',u'王铮':'15274897798',u'刘金莲':'18124720675',u'YY':'13580433642',u'吴彦祖':'15013719143'}

class wechatlanhu(object):
    title=''
    text=''
    url=''
    at=''

    def __init__(self,title,text,url,at):
        self.title = title
        self.text = text
        self.url = url
        self.at = phone[at]

