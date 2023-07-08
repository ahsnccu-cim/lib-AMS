from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi('Um+j6LIGrYlkzgZEvrzkBH8oP63xpFcU1SSqSoe+/yqIgceEi/c1VUyvtHKey76k6dvYytHDXE+bBwedSuFB8vOf8RLNgkp3wwwD2hqpXh1R610ccSQs3Uh3nKCCJS58zrRqJjPO9uWrNfTQagXg4wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('29e55b0c7da115511974b1b325e4b75f')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@傳送文字':
        try:
            message = TextSendMessage(  
                text = "目前還沒完成:(\n以後再說！"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

__name__ == '__main__';
app.run()            
        
