from flask import Flask
from linebot import (
    LineBotApi, WebhookParser
)
from flask_sqlalchemy import SQLAlchemy
import os
#### fill your current project name
current_project = 'diseno-test-project'

app = Flask(__name__)
db = SQLAlchemy(app)

from Project.GDRIVE_API.connect import create_connection
from Project.GDRIVE_API.Download import Transfer_file_to_Gdrive


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '{}.sqlite'.format(create_connection(current_project)))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#### must be initialize current project ####
host_name = 'https://testappbook.herokuapp.com'


#### path to static file 
app.config['project_dir'] = 'Project\static'



# your bot key

bot_access_key = '1RfIiAbjneORMpj+sIGYx+Yi0esjdG/F/VQxyIc6/dFoCVym6hZzDrBqxpd5Ui8XFLsdzohfRuvZRU1dsCP0yaSN3Rdx7U3PeT/0kZfnkrAXrmtrclZaw0v/tA6vOe2fM93R+JvDab5xhxN/4vtGYQdB04t89/1O/w1cDnyilFU='
bot_secret_key = '31d9c964d1afd080749b16d09f2f016c'

line_bot_api = LineBotApi(bot_access_key)
parser = WebhookParser(bot_secret_key)
    
from Project import routes
from Project.GDRIVE_API.google_drive_api import Project_Gdrive


    
    