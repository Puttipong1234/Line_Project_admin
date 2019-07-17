from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser

from flask import request, abort

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,FlexSendMessage , JoinEvent , QuickReply , QuickReplyButton , MessageAction , URIAction
)


from Project import app , Line_bot_user_id , current_project
from Project import line_bot_api,parser
from Project.RichMenu import menuList,postmenu

### flex content sender ####
from Project.UI.Menu import * 


## main event for line chatbot ##
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        events = parser.parse(body, signature)

    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    for event in events:
        user_id= event.source.sender_id

        Quick_Reply = QuickReply(items=[
                                #    QuickReplyButton(action=URIAction(label="ดูแบบก่อสร้างล่าสุด", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : DRAWING'))),
                                #    ##### สร้างเมนู โมเดล 3 มิติ
                                #    QuickReplyButton(action=URIAction(label="ดูโมเดล อาคาร 3 มิติ", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : 3D_MODEL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูรายละเอียดวัสดุ", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : MATERIAL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูเอกสาร APPROVAL", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : APPROVAL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูใบเสนอราคา", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : QUOTATION'))),
                                #    QuickReplyButton(action=URIAction(label="ไปที่หน้าหลักโครงการ", uri='line://ti/p/{}'.format(Line_bot_user_id)))
                                    QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')),
                                    QuickReplyButton(action=MessageAction(label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')),
                                    QuickReplyButton(action=MessageAction(label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')),
                                    QuickReplyButton(action=MessageAction(label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL'))
                               ])

        ## change rich menu
        # if isinstance(event, MessageEvent):
        
        if isinstance(event, MessageEvent) and TextMessage is type(event.message):
            menuname = event.message.text
            
            print(event.type)
            if menuname == 'เลือก Menu : DRAWING':
                data = SetMessage_From_Database('drawing')
                send_flex(event.reply_token,data)
                return '200'
            if menuname == 'เลือก Menu : MATERIAL':
                data = SetMessage_From_Database('material')
                send_flex(event.reply_token,data)
                return '200'
            if menuname == 'เลือก Menu : PAYMENT':
                data = SetMessage_From_Database('payment')
                send_flex(event.reply_token,data)
                return '200'
            if menuname == 'เลือก Menu : APPROVAL':
                data = SetMessage_From_Database('approval')
                send_flex(event.reply_token,data)
                return '200'
            if menuname == 'เลือก Menu : QUOTATION':
                data = SetMessage_From_Database('quotation')
                print(data)
                send_flex(event.reply_token,data)
                return '200'
            if menuname == 'เลือก Menu : 3D_MODEL':

                contents = {
                    'โมเดลสถาปัถ' : 'https://viewer.autodesk.com/',
                    'โมเดลโครงสร้าง' : 'https://viewer.autodesk.com/',
                    'โมเดลงานระบบ' : 'https://viewer.autodesk.com/',
                    'โมเดล combine ' : 'https://viewer.autodesk.com/'
                }


                data = SetSingleColumnMenu(contents)
                send_flex(event.reply_token,data)
                return '200'
            postmenu(menuname,user_id)
        ## change rich menu
        if isinstance(event, FollowEvent):
            menuname = 'back'
            postmenu(menuname,user_id)
            return '200'

        ## menu ใน group chat
        if isinstance(event,JoinEvent):
            print('line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : DRAWING'))
            print('line://ti/p/{}'.format(Line_bot_user_id))
            Button_Reply = TextSendMessage(text='ยินดีต้องรับสู่บริการ Project Assistance โครงการ {} ยินดีรับใช้ กรุณากดปุ่มเพื่อเลือกเมนู'.format(current_project),
                               quick_reply=Quick_Reply)
            line_bot_api.reply_message(event.reply_token,messages = Button_Reply)
            return '200'
        
        else :
            Button_Reply = TextSendMessage(text='ยินดีต้องรับสู่บริการ Project Assistance โครงการ {} ยินดีรับใช้ กรุณากดปุ่มเพื่อเลือกเมนู'.format(current_project),
                               quick_reply=Quick_Reply)
            line_bot_api.reply_message(event.reply_token,messages = Button_Reply)
        
    return '200'








