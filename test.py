template = {
        "type": "bubble",
        "direction": "ltr",
        "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "text",
            "text": 'column_name',
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
                "text": 'folder_link'
            },
            "flex": 5,
            "style": "primary"
            },
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "DEL",
                "text": 'folder_link'
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

print(template['body']['contents'])