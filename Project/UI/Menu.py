file_data = {"replyToken":'', "messages": []}


import json
import requests
from Project.UI.Flex_Template import each_file_in_list , each_Column_in_carousel , Carousel_menu
from Project import app
import os
from Project import db , bot_access_key
from Project.GDRIVE_API.models import *
from Project.GDRIVE_API.google_drive_api import Project_Gdrive


def SetMenuMessage_Object(file_data,Message_data):
    file_data['message'].append(Message_data)
    return file_data

def SetMessage_From_Database(folder_name):
    _menus = Menu.query.filter_by(name = folder_name).first()
    _submenus = Submenu.query.filter_by(menu = _menus).all()
    project = Project_Gdrive()
    all_file = project.GetFile_FromFolderName(folder_name)
    Columns = []
    files = []
    for col in _submenus:
      for num,_file in enumerate(all_file):
        num = num + 1
        files.append(each_file_in_list(str(num),_file['title'],_file['alternateLink']))
        print(num,_file['title'],_file['alternateLink'])
      #### foldername or column name col['alternateLink']
      result = each_Column_in_carousel(folder_name,col['alternateLink'],files)
      Columns.append(result)
    Carousel_message = Carousel_menu(Columns)
    message = SetMenuMessage_Object(files,Carousel_message)
    return message
    ### return message_carousel_data to send flex





### send_flex message with list of content inside
def send_flex(reply_token,file_data):

    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(bot_access_key)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}

    file_data['replyToken'] = reply_token
    #### dumps file จาก dict ให้เป็น json
    file_data = json.dumps(file_data)

    r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    return print(r.text)