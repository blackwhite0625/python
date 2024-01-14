from flask import Flask, request
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    try:    
        json_data = json.loads(body)
        access_token = 'Qjjwyaz8ciexiBYh36CLyW1gDtxIOPT+CreuDjq7LAZ7SgCmtfLYm6pzd7bysVnstBy0o471kj8hCyMZZnIT90o1E333EgRvkWwEo8LcTl4svihyi0NLGB8SXFSM+EUDV5FJTfUtGH5/tCnzMdC1wwdB04t89/1O/w1cDnyilFU='
        secret = 'ff842537aa23564f908e6418e129eb22'
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        
        tk = json_data['events'][0]['replyToken']
        type = json_data['events'][0]['message']['type']
        if type == 'text':
            msg = json_data['events'][0]['message']['text']
            print(msg)
            reply = msg
        else:
            reply = '不是文字'
        print(reply)
        line_bot_api.reply_message(tk, TextSendMessage(reply))
    except:
        print(body)
    return 'OK'

if __name__ == "__main__":
    app.run()
