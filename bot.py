import telegram 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
from token_data import token_value as tv


def help(update, context):
    text_send = 'To create your timetable, write "/reg NAME".\nTo see your timetable, write /tt.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)


def reg(update, context):
    get_name(update, context)
    #    text_send = "Write /fn YOUR_FIRST_NAME"
#    print(context)
#    name = context.args[0]
#    if name is None:
#        text_send = 'You didn\'t write your name. Please, write "/reg NAME" again.'
#    elif str.isnumeric(name) is True:
#        text_send = ''
#    print(name)


def get_name(update, context):
    text_send = "Write command name:"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

    

def echo(update, context):
    text_send = "Write /help, plz"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)


def timetable(update, context):
    text_send = 'Here will be your timetable'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

"""
def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    
#    query.edit_message_text(text="Selected option: {}".format(query.data))

#    if query.data == 'timetable':
#        reply_markup = CallbackQueryHandler(timetable)
#        query.edit_message_text(text="cool", reply_markup=reply_markup)
"""


token = tv()
bot = telegram.Bot(token=token)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
updater.start_polling()

############################ HANDLERS ##############################

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

registration_handler = CommandHandler('reg', reg)
dispatcher.add_handler(registration_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

timetable_handler = CommandHandler('timetable', timetable)
dispatcher.add_handler(timetable_handler)

tt_handler = CommandHandler('tt', timetable)
dispatcher.add_handler(tt_handler)

#button_handler = CallbackQueryHandler(button)
#dispatcher.add_handler(button_handler)
############################ HANDLERS ##############################
