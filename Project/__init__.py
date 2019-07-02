from flask import Flask
from linebot import (
    LineBotApi, WebhookParser
)

app = Flask(__name__)

line_bot_api = LineBotApi('1RfIiAbjneORMpj+sIGYx+Yi0esjdG/F/VQxyIc6/dFoCVym6hZzDrBqxpd5Ui8XFLsdzohfRuvZRU1dsCP0yaSN3Rdx7U3PeT/0kZfnkrAXrmtrclZaw0v/tA6vOe2fM93R+JvDab5xhxN/4vtGYQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('31d9c964d1afd080749b16d09f2f016c')
from Project import routes

    