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
    #replyStack.append('นี่คือรูปแบบข้อความที่รับส่ง')
    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    
    if(str(msg_in_json["events"][0]["message"]["text"]) == "คุณกำลังมองหาอะไรอยู่"):
      replyStack.append('คุณสามารถพิมพ์สินค้าที่คุณสนใจเพื่อค้นหาโปรโมชั่นดีๆได้')
    if(str(msg_in_json["events"][0]["message"]["text"]) == "หาร้านแนะนำ"):
      replyStack.append('แถวๆนี้ มีร้านป้าแก้วไก่กรอบ ห่างออกไป 1 กม. บัตรกรุงศรีของคุณมีส่วนลด 20 เปอร์เซนต์')
    if(str(msg_in_json["events"][0]["message"]["text"]) == "ร้านค้าออนไลน์"):
      replyStack.append('บัตรกรุงศรีของคุณมีส่วนลด 15% เพียงคุณสั่งซื้อของจากร้าน 11street')
    if(str(msg_in_json["events"][0]["message"]["text"]) == "ตั้งค่า"):
      replyStack.append('คุณสามารถทำการตั้งค่าได้ดังนี้\n1. เพิ่มบัตรเครดิต\n2. ตั้งค่าการแจ้งเตือน')
    if(str(msg_in_json["events"][0]["message"]["text"]) == "รองเท้า"):
     replyStack.append('รองเท้า nike กำลังลดราคา 10% เพียงจ่ายผ่านบัตรกรุงศรี click : https://shopee.co.th/Nike-Roshe-One-Women's-and-Men's-Running-Shoes-Sneakers-Grey-white-i.29977109.519526526')
    if(str(msg_in_json["events"][0]["message"]["text"]) == "กระเป๋า"):
     replyStack.append('มีกระเป๋า กำลังลดราคา 10% เพียงจ่ายผ่านบัตรกรุงศรี click : https://shopee.co.th/%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9B%E0%B9%8B%E0%B8%B2%E0%B8%84%E0%B8%AD%E0%B8%A1%E0%B8%9E%E0%B8%B4%E0%B8%A7%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B8%B9%E0%B8%99-%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9B%E0%B9%8B%E0%B8%B2%E0%B8%96%E0%B8%B7%E0%B8%AD-laptop-bag-Cartoon-i.24756900.784553265?ads_keyword=%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9B%E0%B9%8B%E0%B8%B2%E0%B8%96%E0%B8%B7%E0%B8%AD&adsid=40239&campaignid=40294&position=0')

    
    
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
