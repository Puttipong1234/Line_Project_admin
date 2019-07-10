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

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '{}.sqlite'.format(current_project))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#### must be initialize current project ####
host_name = 'https://testappbook.herokuapp.com'


#### path to static file 
app.config['project_dir'] = 'Project\static\Project'
app.config['drawing_dir'] = 'Project\static\Project\{}\drawing'.format(current_project)
app.config['payment_dir'] = 'Project\static\Project\{}\payment'.format(current_project)
app.config['material_dir'] = 'Project\static\Project\{}\material'.format(current_project)
app.config['approval'] = 'Project\static\Project\{}\\approval'.format(current_project)


# your bot key
line_bot_api = LineBotApi('1RfIiAbjneORMpj+sIGYx+Yi0esjdG/F/VQxyIc6/dFoCVym6hZzDrBqxpd5Ui8XFLsdzohfRuvZRU1dsCP0yaSN3Rdx7U3PeT/0kZfnkrAXrmtrclZaw0v/tA6vOe2fM93R+JvDab5xhxN/4vtGYQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('31d9c964d1afd080749b16d09f2f016c')

from Project import routes

if __name__ == '__main__':
    if os.path.isfile('{}.sqlite'.format(current_project)):
        db.create_all()
    else :
        pass
    