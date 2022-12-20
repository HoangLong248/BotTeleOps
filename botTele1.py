from telegram import *
from telegram.ext import *
# import requests import *
import logging, sys

def create_log(path_filename, getLogger):
    # create logger with 'debug'
    logger = logging.getLogger(getLogger)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    inf_log = logging.FileHandler(path_filename)
    inf_log.setLevel(logging.INFO)

    # create console handler with a higher log level
    stream_log = logging.StreamHandler(stream=sys.stdout)
    stream_log.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('|%(asctime)s|%(name)s|%(levelname)s| %(message)s')
    inf_log.setFormatter(formatter)
    stream_log.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(inf_log)
    logger.addHandler(stream_log)
    return logger

def startCommand(update: Update, context: CallbackContext):
    # print(update.effective_chat.username)
    # print(update.message.text)
    buttons = [[KeyboardButton("Random Image")], [KeyboardButton("Random Person")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome welcom",
    reply_markup=ReplyKeyboardMarkup(buttons))

updater = Updater(token='5026185888:AAGuZmrT4R4unv-F_f5Yj_v7nH32-RXdRaw')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", startCommand))


# logger = create_log('file_bot.log')

updater.start_polling()