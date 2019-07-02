from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources
)

from RichMenu import postmenu 


app = Flask(__name__)

line_bot_api = LineBotApi('1RfIiAbjneORMpj+sIGYx+Yi0esjdG/F/VQxyIc6/dFoCVym6hZzDrBqxpd5Ui8XFLsdzohfRuvZRU1dsCP0yaSN3Rdx7U3PeT/0kZfnkrAXrmtrclZaw0v/tA6vOe2fM93R+JvDab5xhxN/4vtGYQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('31d9c964d1afd080749b16d09f2f016c')


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

    return 'OK'


    for event in events:
        if event.source.type == 'user':
            user_id = event.source['user']
            print(user_id)
            menuname = event.message.text
            print(menuname)
            postmenu(user_id,menuname)


    return 'OK'


