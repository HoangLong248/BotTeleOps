# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
# from telegram

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Water", callback_data='Water'),InlineKeyboardButton("Evn", callback_data='Evn')],
                [InlineKeyboardButton("Telecom", callback_data='Telecom'),InlineKeyboardButton("HCC", callback_data='HCC')],
                [InlineKeyboardButton("School", callback_data='School'), InlineKeyboardButton("Hospital", callback_data='Hospital')],
                [InlineKeyboardButton("Apartment", callback_data='Apartment'),InlineKeyboardButton("Hospital", callback_data='Hospital')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update, context):

    # if query option exists when add_handler is CallbackQueryHandler ex: updater.dispatcher.add_handler(CallbackQueryHandler(button))
    query = update.callback_query
    print(query.data)
    context.bot.editMessageText(text="Selected option: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def step2(update, context):
    print(update)
    query = update.effective_message
    print(query)

def help(update, context):
    update.message.reply_text(text="Use /start to test this bot.")

# def error(bot, update, error):
#     logging.warning('Update "%s" caused error "%s"' % (update, error))

# Create the Updater and past it your bot's token.
updater = Updater("5181574497:AAECXpM8JLPFYtjHpp_Tx0CnVvdHvIF1C-Y")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CallbackQueryHandler(step2))
updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()