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
,FlexSendMessage
)


from Project import app
from Project import line_bot_api,parser
from Project.RichMenu import menuList,postmenu

### flex content sender ####
from Project.UI.Menu import send_flex, file_data, SetMenuMessage_Object ,SetMessage_From_Database


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

        ## change rich menu
        # if isinstance(event, MessageEvent):
        if isinstance(event, MessageEvent) and TextMessage is type(event.message):
            menuname = event.message.text
            postmenu(menuname,user_id)
            if event.message.text == 'เลือก Menu : DRAWING':
                data = SetMessage_From_Database('drawing')
                send_flex(event.reply_token,data)
            
            if event.message.text == 'เลือก Menu : MATERIAL':
                data = SetMessage_From_Database('material')
                send_flex(event.reply_token,data)
            
            if event.message.text == 'เลือก Menu : PAYMENT':
                data = SetMessage_From_Database('payment')
                send_flex(event.reply_token,data)
            
            if event.message.text == 'เลือก Menu : APPROVAL':
                data = SetMessage_From_Database('approval')
                send_flex(event.reply_token,data)
            
            if event.message.text == 'เลือก Menu : QUOTATION':
                data = SetMessage_From_Database('quotation')
                send_flex(event.reply_token,data)
                
        ## change rich menu
        if isinstance(event, FollowEvent):
            menuname = 'back'
            postmenu(menuname,user_id)










