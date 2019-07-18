#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
import json
import sys
import os
import subprocess
import requests
from linebot.models import *
from linebot.models.template import *
from Project import line_bot_api


def create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,ActionList):
    rich_menu = RichMenu()
    height = 1686
    width = 2500
    rich_menu.size = {'width':width,'height':height}
    rich_menu.selected = False
    rich_menu.name = mname
    rich_menu.chatBarText = mchatbar
    xstep = width/ncol
    ystep = height/nrow
    nitem = nrow*ncol
    areaList = []
    for i in range(nrow):
        y = ystep*i
        for j in range(ncol):
            x = xstep*j
            rbound = RichMenuBounds(x,y,xstep,ystep)
            rAction = Action()
            try:
                actionComp = ActionList[ncol*i+j]
                if actionComp.find('://')!=-1:
                    rAction.type = 'uri'
                    rAction.uri = actionComp
                else:
                    rAction.type = 'message'
                    rAction.text = actionComp
                ar = RichMenuArea()
                ar.action = rAction
                ar.bounds = rbound
                areaList.append(ar)
            except:
                break
    rich_menu.areas = areaList
    menuId = line_bot_api.create_rich_menu(rich_menu)
    contentType = 'image/jpeg'
    img = open(mimage,'rb').read()
    line_bot_api.set_rich_menu_image(menuId,contentType,img)
    return menuId


# def create_teacher_menu():
#     mname = 'สอนหนังสือ'
#     mchatbar = 'สอนหนังสือ'
#     mimage='botnoimenu.jpg'
#     nrow=2
#     ncol=3
#     textList = ['เมนูหลัก','สอนภาษาอังกฤษ','สอนคณิตศาสตร์','สอนวิทยาศาสตร์','สอนสังคม','สอนภาษาไทย']
#     return create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,textList)

# def create_personal_menu():
#     mname = 'บอทส่วนตัว'
#     mchatbar = 'บอทส่วนตัว'
#     mimage='botnoimenu.jpg'
#     nrow=2
#     ncol=2
#     textList = ['เมนูหลัก','บอทน้อยส่วนตัว','ผองเพื่อนบอทน้อย','http://line://msg/text/?']
#     return create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,textList)

# def create_mainmenu():
#     name = 'เมนูหลัก'
#     chatbar = 'เมนูหลัก'
#     image = 'Project\static\งานนำเสนอ1\Slide1.JPG'
#     nrow = 2
#     ncol = 3
#     actionlist = ['project info','เลือก Menu : DRAWING','Today report','project staff','เลือก Menu : MATERIAL','admin zone']
#     return create_richmenu_generic(name,chatbar,image,nrow,ncol,actionlist)

def create_mainmenu():
    name = 'เมนูหลัก'
    chatbar = 'เมนูหลัก'
    image = 'Project\static\งานนำเสนอ1\Slide2.JPG'
    nrow = 2
    ncol = 3
    actionlist = ['เลือก Menu : 3D_MODEL','เลือก Menu : 3D_MODEL','เลือก Menu : DRAWING','เลือก Menu : 3D_MODEL','เลือก Menu : 3D_MODEL','admin zone']
    return create_richmenu_generic(name,chatbar,image,nrow,ncol,actionlist)

def create_adminmenu():
    name = 'จัดการข้อมูล'
    chatbar = 'เมนูผู้บริหาร'
    image = 'Project\static\งานนำเสนอ1\Slide3.JPG'
    nrow = 2
    ncol = 3
    actionlist = ['เลือก Menu : PROJECT STATUS','เลือก Menu : STAFF','เลือก Menu : PAYMENT','เลือก Menu : APPROVAL','เลือก Menu : QUOTATION','back']
    return create_richmenu_generic(name,chatbar,image,nrow,ncol,actionlist)



menuList = {}
#back to menu
menuList['back'] = 'richmenu-15c7d10357c28fa41eb0a9b58702c274'
#direct to admin zone
menuList['admin zone'] = 'richmenu-a254d75a1420f5896df64c900592d6bd'


def postmenu(menuName,userId='xxx'):
    menuId = menuList[menuName]
    print(menuId)
    line_bot_api.link_rich_menu_to_user(userId,menuId)
    return print('done')



    