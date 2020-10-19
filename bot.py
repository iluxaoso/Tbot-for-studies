import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from token_data import token_value as tv


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def timetable(update, context):
    text_send = 'Here will be your timetable'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

"""
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
"""

token = tv()
bot = telegram.Bot(token=token)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

############################ HANDLERS ##############################

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

timetable_handler = CommandHandler('timetable', timetable)
dispatcher.add_handler(timetable_handler)

"""
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
"""

############################ HANDLERS ##############################



