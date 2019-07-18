from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,FlexSendMessage , JoinEvent , QuickReply , QuickReplyButton , MessageAction , URIAction
)

import json


def get_quickreply_template():
    Quick_Reply = QuickReply(items=[
                                        QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')),
                                        QuickReplyButton(action=MessageAction(label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')),
                                        QuickReplyButton(action=MessageAction(label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')),
                                        QuickReplyButton(action=MessageAction(label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL'))
                                ])
    # return Quick_Reply.__dict__
    data = Quick_Reply.as_json_string()
    return json.loads(data)

### input lsit of quick actions
def Quick_Reply_Schema():
    Quick_Actions = get_quickreply_template()
    template = {
        "quickReply": {
    "items": []
    }
    }
    
    template["quickReply"]["items"] = Quick_Actions['items']
    return template

data = {
  "type": "text",
  "text": "Select your favorite food category or send me your location!"
}


data.update(Quick_Reply_Schema())
print(data)