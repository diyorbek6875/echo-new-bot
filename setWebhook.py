import telegram
url="https://mardon.pythonanywhere.com/bot/"
TOKEN="6190918955:AAED-3niA2qqmsmDZmWFAEDcLKRmmys9eTs"
bot=telegram.Bot(token=TOKEN)
bot.delete_webhook()
print(bot.set_webhook(url))