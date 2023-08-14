from flask import Flask,request
import requests
app = Flask(__name__)
@app.route("/bot")
def hello():
    if request.method=="POST":
        data=request.get_json()
        chat_id=data["message"]["chat"]["id"]
        url="https://api.telegram.org/bot6089863461:AAGuL8gKw5QdjXaqwcNY6dZmQmezYVgtDUg/sendMessage"
        payload={
            "chat_id":chat_id,
            "text":data["message"]['text']
        }
        requests.get(url,params=payload)
        return 'OK'
if __name__ == "__main__":
    app.run(debug=True)