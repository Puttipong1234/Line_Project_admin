from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser

from flask import request, abort , send_from_directory

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,FlexSendMessage , JoinEvent , QuickReply , QuickReplyButton , MessageAction , URIAction
)


from Project import app , Line_bot_user_id , current_project , Project_Picture
from Project import line_bot_api,parser
from Project.RichMenu import menuList,postmenu

### flex content sender ####
from Project.UI.Menu import * 


quickReply = QuickReply(items=[
    QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')),
    QuickReplyButton(action=MessageAction(label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')),
    QuickReplyButton(action=MessageAction(label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')),
    QuickReplyButton(action=MessageAction(label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL'))
    ])


Command_list = ['ขอแบบ','ขอเอกสาร','ขอข้อมูล','ขอโมเดล','ขอรายการ']
def Check_command(menuname):
    for i in Command_list:
        if i in menuname:
            return True



## main event for line chatbot ##
@app.route("/", methods=['POST','GET'])
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

        ## change rich menu
        # if isinstance(event, MessageEvent):
        
        if isinstance(event, MessageEvent) and TextMessage is type(event.message):
            menuname = event.message.text
            
            print(event.type)
            if menuname == 'เลือก Menu : DRAWING':
                data = SetMessage_From_Database('drawing',Quick_Reply= True)
                send_flex(event.reply_token,data)
                return '200'
            elif menuname == 'เลือก Menu : MATERIAL':
                data = SetMessage_From_Database('material',Quick_Reply= True)
                send_flex(event.reply_token,data)
                return '200'
            elif menuname == 'เลือก Menu : PAYMENT':
                data = SetMessage_From_Database('payment',Quick_Reply= True)
                send_flex(event.reply_token,data)
                return '200'
            elif menuname == 'เลือก Menu : APPROVAL':
                data = SetMessage_From_Database('approval',Quick_Reply= True)
                send_flex(event.reply_token,data)
                return '200'
            elif menuname == 'เลือก Menu : QUOTATION':
                data = SetMessage_From_Database('quotation',Quick_Reply= True)
                send_flex(event.reply_token,data)
                return '200'
            elif menuname == 'เลือก Menu : 3D_MODEL':

                contents = {
                    'อาคาร 1' : 'https://viewer.autodesk.com/id/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YTM2MHZpZXdlci90NjM2OTkxMjMxNjk0NjgwODY5XzZhZjlkMmJlLTZkMTEtNDhhYy05OWM4LTc4NThmNzMyNWU1My5ydnQ?designtype=rvt&sheetId=NDIyMGU3YjEtYTQ5NC1hMDEwLTVmNDItY2QzMDk1MGM1MTc1',
                    'อาคาร 2' : 'https://viewer.autodesk.com/id/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6YTM2MHZpZXdlci90NjM2OTkxMjM2MTI0NjY2OTY4X2E5Yzc0ZmNhLTJhNjgtNGIyNC1iMWYzLWNiYTE5YWE3MTJkNy5ydnQ?designtype=rvt&sheetId=NTJiNTE0YTMtMjAwNi00OTJkLTk0MTQtOTRjZmZjZTg1NDBjLTAwMDgzZDhm',
                }


                data = SetSingleColumnMenu(contents)
                send_flex(event.reply_token,data)
                return '200'

            elif Check_command(menuname) :
                Button_Reply = TextSendMessage(text='บริการเลขาอัจริยะ กรุณาเลือกเมนูเบื้องต้นที่สามารถช่วยท่านได้ หรือไปที่หน้าแรกโครงการ คลิกที่ Link >> line://ti/p/{} <<'.format(Line_bot_user_id),
                               quick_reply=quickReply)
                line_bot_api.reply_message(event.reply_token,messages = Button_Reply)

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
                               quick_reply=quickReply)
            line_bot_api.reply_message(event.reply_token,messages = Button_Reply)
            
            return '200'
        
    return '200'


# host project image
@app.route('/PIC/<filename>')
def return_Pic(filename):
    filename = Project_Picture
    return send_from_directory('static',filename)




