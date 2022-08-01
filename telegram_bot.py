from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode
import re

# BOT Token or API KEY
BOT_TOKEN = "BOT_TOKEN:OR_API_KEY_HERE"

# GROUP OR Chat Id
GROUP_ID = "CHAT_ID_HERE"

bot = Bot(BOT_TOKEN)
# print(bot.get_me())

updater = Updater(BOT_TOKEN, use_context=True)
 
dispatcher: Dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="Welcome to our bot")

def get_id(update, context):
    bot.send_message(chat_id=update.effective_chat.id, text=update.message.chat.id)

def reply_to(update, context):
    args = context.args
    if len(args) > 1:
        id, *text = args
        bot.send_message(chat_id=id, text=" ".join(text),  parse_mode=ParseMode.HTML)

def on_voice(update, context):
    print(update.message)
    chat = update.message.chat
    if chat.id != int(GROUP_ID):
        voice = update.message.voice
        bot.send_voice(chat_id=GROUP_ID, voice=voice)

def on_message(update, context):
    chat = update.message.chat
    text = update.message.text
    text = "<b>Message from </b>@%s ( %s ): %s" % (chat.username, chat.id, text)
    if chat.id != int(GROUP_ID):
        bot.send_message(chat_id=GROUP_ID, text=text, parse_mode=ParseMode.HTML)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("get_id", get_id))
dispatcher.add_handler(CommandHandler("reply_to", reply_to))
dispatcher.add_handler(MessageHandler(Filters.voice, on_voice))
dispatcher.add_handler(MessageHandler(Filters.text, on_message))

updater.start_polling()
