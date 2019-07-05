
from Project import host_name


def each_drawing_in_list(number,drawing_name,url):
    drawing_template =  {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "{number}",
                "align": "center",
                "gravity": "center"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "{drawing_name}",
                "uri": "{url}"
                },
                "flex": 10
            }
            ]
        }
    drawing_template['contents'][0]['text'] = number
    drawing_template['contents'][1]['label'] = drawing_name
    drawing_template['contents'][1]['uri'] = url
    return drawing_template

