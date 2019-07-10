drawing_data = {"replyToken":'', "messages": []}


import json
import requests
from Project.UI.Flex_Template import each_drawing_in_list , each_Column_in_carousel , Carousel_menu
from Project import app
import os


def update_Carousel_menu(drawing_data,Carousel_data):
    drawing_data['message'].append(Carousel_data)
    return drawing_data


### send_flex message with list of content inside
def send_flex(reply_token,drawing_data):

    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer 1RfIiAbjneORMpj+sIGYx+Yi0esjdG/F/VQxyIc6/dFoCVym6hZzDrBqxpd5Ui8XFLsdzohfRuvZRU1dsCP0yaSN3Rdx7U3PeT/0kZfnkrAXrmtrclZaw0v/tA6vOe2fM93R+JvDab5xhxN/4vtGYQdB04t89/1O/w1cDnyilFU='

    headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}

    drawing_data['replyToken'] = reply_token
    #### dumps file ให้เป็น
    drawing_data = json.dumps(drawing_data)

    r = requests.post(LINE_API, headers=headers, data=drawing_data) # ส่งข้อมูล

    return print(r.text)