from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources
)

from Project.RichMenu import postmenu 


from Project import app

from Project import line_bot_api,parser


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
        print(events)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

################### cannot read event ################
    for event in events:
        print(event)
        print(event.source)
        user_id = event.source['user']
        print(user_id)
        menuname = event.message.text
        print(menuname)
        postmenu(user_id,menuname)


    return 'OK'


