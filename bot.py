import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import urllib.request
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def start_bot(update, context):
    update.message.reply_text("бот старт")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.replay_text(text)

def get_ip(update, context):
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    update.message.reply_text(f"{external_ip}")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(CommandHandler("get_ip", get_ip))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

if __name__== "__main__":
    main()