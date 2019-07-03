from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,JoinEvent
)


from Project import app

from Project import line_bot_api,parser

menuList = {}
menuList['Project Info'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['Drawing'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['Payment'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['approval'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['material'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['admin zone'] = 'richmenu-f38c34eb1c8f90efa86d0c46083e014b'
menuList['back'] = 'richmenu-7c7946aded99dab8c2ab94986b6a0c1d'



def postmenu(menuName,userId='xxx'):
    menuId = menuList[menuName]
    print(menuId)
    line_bot_api.link_rich_menu_to_user(userId,menuId)
    return print('done')




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


################### cannot read event ################

    for event in events:
        user_id= event.source.sender_id

        menuname = event.message.text
        print(menuname)
        if not isinstance(event, MessageEvent):
            postmenu(menuname,user_id)


        if not isinstance(event, JoinEvent):
            line_bot_api.link_rich_menu_to_user(user_id,'richmenu-7c7946aded99dab8c2ab94986b6a0c1d')

    

    return 'OK'


