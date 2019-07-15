
def each_file_in_list(number,file_name,url):
    template =  {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": number,
                "align": "center",
                "gravity": "center"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": file_name,
                "uri": url
                },
                "flex": 10
            }
            ]
        }
    return template

## create Column by name and its content
def each_Column_in_carousel(column_name,folder_link,content): ## ชื่อของเมนู กับ content คือ list ของeach file in list
    template = {
        "type": "bubble",
        "direction": "ltr",
        "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "text",
            "text": column_name,
            "size": "xxl",
            "align": "center",
            "gravity": "center",
            "color": "#FFFFFF"
            }
        ]
        },
        "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "lg",
        "contents": [
            {
            "type": "box",
            "layout": "horizontal",
            "spacing": "none",
            "contents": [
                {
                "type": "text",
                "text": "No.",
                "align": "start"
                },
                {
                "type": "separator"
                },
                {
                "type": "text",
                "text": "Name",
                "flex": 6,
                "align": "center"
                },
                {
                "type": "separator"
                },
                {
                "type": "spacer"
                }
            ]
            }
        ]
        },
        
        "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "UPLOAD",
                "text": folder_link
            },
            "flex": 5,
            "style": "primary"
            },
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "DEL",
                "text": folder_link
            },
            "flex": 0,
            "color": "#FF0000",
            "margin": "lg",
            "style": "primary"
            }
        ]
        },
        "styles": {
        "header": {
            "backgroundColor": "#323232"
        }
        }
    }
    
    
    for i in content:
        template['contents']['body']['contents'].append(i)
    
    return template


## Create Carousel message 
def Carousel_menu(columns):
    template = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": []
  }
    }
    for i in columns:
        template['contents']['contents'].append(i)
    return template
