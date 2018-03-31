from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
LINE_API_KEY = 'Bearer hQc9utCXyk6y+TvGoZqF37Tp0PkfEDQfVgFAIsJr2wBgd/yg7QbEkcHhohBbq6yJNPJHnrVJHEzQHNDoTNdOefpSA1jXaMo0q3jEP/3UYm8JVdV9Valg6FoY9s5e8Xik8CsldbTu/R2cYJLvd2NlGwdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyStack = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']

    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    replyStack.append('นี่คือรูปแบบข้อความที่รับส่ง')
    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyStack.append(str(msg_in_json["events"][0]))
 
    reply(replyToken, replyStack[:5])
    
    return 'OK',200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
