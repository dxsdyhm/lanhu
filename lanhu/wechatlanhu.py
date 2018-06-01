phone={'墨香':'13128756863','神秘圆圆酱':'17665310095','学无止境':'15270628776','王铮':'15274897798','刘金莲':'18124720675','YY':'13580433642','吴彦祖':'15013719143'}

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

