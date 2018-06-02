# coding:utf-8
import json
import requests
from wxpy import *
import re

from lanhu.wechatlanhu import wechatlanhu

bot = Bot()

# 机器人账号自身
myself = bot.self
# <title><![CDATA[新评价通知]]></title>
# <des><![CDATA[在【演示项目】项目中有同事@了你~\n职位名称：同事\n评价人：墨香\n评价时间：2018.06.01 09:58\n对设计图【设计图  B】评论"@墨香 这是文本内容..."]]></des>
des="<des><!\\[CDATA\\[(.+?)\\]\\]></des>"
name=u"评论\\\"@(.+) "
lanhu_url="http://45.77.198.212/lanhuat"
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}

def changeBody(data):
    print(data)
    return json.dumps(data)

@bot.register()
def forward_boss_message(msg):
    if msg.type==SHARING:
        data = msg.raw
        print(data)
        text=data['Text']
        if text==u'新评价通知':
            lanhudes = re.findall(des, data['Content'], re.S)[0]
            lanhuToUser = re.findall(name, lanhudes)[0]
            lanhudes = lanhudes.replace('"', ":")
            dat = wechatlanhu(data['Text'], lanhudes, data['Url'], lanhuToUser,'0')
            response = requests.post(lanhu_url, data=dat.__dict__)
            print(response)
        else:
            print(text)
    else:
        print (msg.text)
# 堵塞线程
embed()