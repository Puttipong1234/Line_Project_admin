




# def Quick_Button(imageUrl,label,text):
#     template = {
#         "type": "action",
#         "imageUrl": imageUrl,
#         "action": {
#           "type": "message",
#           "label": label,
#           "text": text
#         }
#       }
#     return template





# def Default_Quick_Reply():
#     model_Button = Quick_Button(imageUrl='https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2019/01/img-UCLH.jpg',label='ดูโมเดลอาคาร 3 มิติ',text='เลือก Menu : 3D_MODEL')
#     drawing_Button = Quick_Button(imageUrl='https://4fs0893rxsil3r8n0j24afu1-wpengine.netdna-ssl.com/wp-content/uploads/2012/06/Elevation_drawing_bac.jpg',label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')
#     quotation_Button = Quick_Button(imageUrl='',label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')
#     approval_Button = Quick_Button(imageUrl='',label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL')

#     List = [model_Button,drawing_Button,quotation_Button,approval_Button]
#     Quick_Reply_Schema(List)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FileMessage , ImageMessage , FollowEvent ,sources,FollowEvent,SendMessage
,FlexSendMessage , JoinEvent , QuickReply , QuickReplyButton , MessageAction , URIAction
)

def get_quickreply_template():
    Quick_Reply = QuickReply(items=[
                                        QuickReplyButton(action=MessageAction(label="ดูโมเดลอาคาร 3 มิติ", text='เลือก Menu : 3D_MODEL')),
                                        QuickReplyButton(action=MessageAction(label="ดูแบบก่อสร้างล่าสุด", text='เลือก Menu : DRAWING')),
                                        QuickReplyButton(action=MessageAction(label="ดูใบเสนอราคา", text='เลือก Menu : QUOTATION')),
                                        QuickReplyButton(action=MessageAction(label="ดูเอกสาร APPROVAL", text='เลือก Menu : APPROVAL'))
                                ])
    return Quick_Reply.__dict__

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


# if __name__ == '__main__':
#     print(Quick_Reply_Schema())
    
