import telegram
url="https://mardon.pythonanywhere.com/bot/"
TOKEN="6618036571:AAEfUwyhzOTSCdDWhBMIryuyDkd5lQYoiSQ"
bot=telegram.Bot(token=TOKEN)
bot.delete_webhook()
print(bot.set_webhook(url))
