
import requests
# from google_drive_api import Project_Gdrive
import os
from .google_drive_api import Project_Gdrive
from Project import bot_access_key

def Transfer_file_to_Gdrive(messageid,folder_name,filetype,filename,Permit = 'Public'):

  Project = Project_Gdrive()
    
  LINE_API = 'https://api.line.me/v2/bot/message/{}/content'.format(messageid)

  Authorization = 'Bearer {}'.format(bot_access_key)

  headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}


  r = requests.get(LINE_API, headers=headers ) # ส่งข้อมูล
  open('{}/{}.{}'.format(Project.data_path,filename,filetype), 'wb').write(r.content)

  if Permit == 'Public':
    up = Project.upload_file_Public(folder_name,filetype,filename)
  else :
    up = Project.upload_file_with_permission(folder_name,filetype,filename)


  os.remove('{}/{}.{}'.format(Project.data_path,filename,filetype))

  return print(LINE_API +"\n" + up)