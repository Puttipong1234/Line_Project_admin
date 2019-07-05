from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort, send_from_directory

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
from Project.UI.drawing import send_flex,drawing_data


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
        if isinstance(event, MessageEvent):
            menuname = event.message.text
            print(event.reply_token)
            if menuname == 'drawing':
                send_flex(event.reply_token,drawing_data)
            postmenu(menuname,user_id)
                

        if isinstance(event, FollowEvent):
            menuname = 'back'
            postmenu(menuname,user_id)

    return 'OK'


## Send file from data base to user ##
## drawing
@app.route("/get-drawing/<drawing_name>")
def get_drawing(drawing_name):
    try :
        return send_from_directory(app.config["drawing_dir"], filename=drawing_name, as_attachment=True)
    except :
        return InvalidSignatureError('Error cannot get file from directory')


## payment
@app.route("/get-payment/<payment_name>")
def get_payment(payment_name):
    try :
        return send_from_directory(app.config["payment_dir"], filename=payment_name, as_attachment=True)
    except :
        return InvalidSignatureError('Error cannot get file from directory')


## material
@app.route("/get-material/<material_name>")
def get_material(material_name):
    try :
        return send_from_directory(app.config["material_dir"], filename=material_name, as_attachment=True)
    except :
        return InvalidSignatureError('Error cannot get file from directory')


## approval
@app.route("/get-approval/<approval_name>")
def get_approval(approval_name):
    try :
        return send_from_directory(app.config["approval_dir"], filename=approval_name, as_attachment=True)
    except :
        return InvalidSignatureError('Error cannot get file from directory')