from flask import Flask,request
import requests,telegram
app = Flask(__name__)
@app.route("/bot/", methods=['POST', 'GET'])
def bot():
    if request.method=="POST":
        data=request.get_json()
        chat_id=data["message"]["chat"]["id"]
        url="https://api.telegram.org/bot6190918955:AAH6JhL8iWSkLg77mvBbMUJQ1QqLahJGD_g/sendMessage"
        payload={
            "chat_id":chat_id,
            "text":"salom"
        }
        r=requests.post(url,json=payload)
        print(r.json())
        return {"message":"ok"}
if __name__ == "__main__":
    app.run(debug=True)