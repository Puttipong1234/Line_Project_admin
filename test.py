
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,FlexSendMessage , JoinEvent , QuickReply , QuickReplyButton , MessageAction , URIAction
)

import json

Quick_Reply = QuickReply(items=[
                                #    QuickReplyButton(action=URIAction(label="ดูแบบก่อสร้างล่าสุด", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : DRAWING'))),
                                #    ##### สร้างเมนู โมเดล 3 มิติ
                                #    QuickReplyButton(action=URIAction(label="ดูโมเดล อาคาร 3 มิติ", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : 3D_MODEL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูรายละเอียดวัสดุ", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : MATERIAL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูเอกสาร APPROVAL", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : APPROVAL'))),
                                #    QuickReplyButton(action=URIAction(label="ดูใบเสนอราคา", uri='line://oaMessage/{}/?{}'.format(Line_bot_user_id,'เลือก Menu : QUOTATION'))),
                                #    QuickReplyButton(action=URIAction(label="ไปที่หน้าหลักโครงการ", uri='line://ti/p/{}'.format(Line_bot_user_id)))
                                    QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')),
                                    QuickReplyButton(action=MessageAction(label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')),
                                    QuickReplyButton(action=MessageAction(label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')),
                                    QuickReplyButton(action=MessageAction(label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL'))
                               ])



a = QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')).__dict__



a = {"1" : "book" , "2" : "notebook"}
b = {"3" : "Encyclopedia"}
a.update(b)
print(a)