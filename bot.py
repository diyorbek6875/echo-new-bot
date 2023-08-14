from flask import Flask,request
import requests,telegram
app = Flask(__name__)
@app.route("/bot")
def bot():
    if request.method=="POST":
        data=request.get_json()
        chat_id=data["message"]["chat"]["id"]
        url="https://api.telegram.org/bot6190918955:AAED-3niA2qqmsmDZmWFAEDcLKRmmys9eTs/sendMessage"
        payload={
            "chat_id":chat_id,
            "text":"salom"
        }
        requests.get(url,params=payload)
        return {"message":"ok"}
if __name__ == "__main__":
    app.run(debug=True)