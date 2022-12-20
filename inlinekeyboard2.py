from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

############################### Bot ############################################
def start(bot, update):
  bot.message.reply_text(main_menu_message(),
                         reply_markup=main_menu_keyboard())

# Main menu
def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

def exit_menu(bot, update):
    bot.callback_query.message.edit_text("Bye Bye!!!",
                          reply_markup=exit_menu_keyboard())

def billpay_menu(bot, update):
    chat_id = bot.callback_query.message.chat_id
    message_id = bot.callback_query.message.message_id
    update.bot.delete_message(chat_id=chat_id, message_id=message_id)
    update.bot.send_message(chat_id=chat_id, text = "Billpay Menu", reply_markup=menu_billpay_keyboard())

def telco_menu(bot, update):
  bot.callback_query.message.edit_text(second_menu_message())

# Billpay Func Menu
def check_service_billpay_maintain(bot, update):
    chat_id = bot.callback_query.message.chat_id
    message_id = bot.callback_query.message.message_id
    update.bot.delete_message(chat_id=chat_id, message_id=message_id)
    update.bot.send_message(chat_id=chat_id, text = "List Group Service", reply_markup=group_serivce_billpay_menu_keyboard())

def list_service_and_check(bot, update):
    chat_id = bot.callback_query.message.chat_id
    message_id = bot.callback_query.message.message_id
    group_service  = bot.callback_query.data
    update.bot.delete_message(chat_id=chat_id, message_id=message_id)
    update.bot.send_message(chat_id=chat_id, text = "List Service {} ".format(group_service.upper()), reply_markup=list_serivce_billpay_menu_keyboard(group_service))
    update.bot.send_message(chat_id=chat_id, text = "")
    print(bot)
# Telco Func Menu

# Error handler
def error(update, context):
    print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Billpay', callback_data='billpay'), InlineKeyboardButton('Telco', callback_data='telco')],
              [InlineKeyboardButton('Exit', callback_data='exit')]]
  return InlineKeyboardMarkup(keyboard)

def menu_billpay_keyboard():
    keyboard = [[InlineKeyboardButton('Check Service Maintain', callback_data='check')],
                [InlineKeyboardButton('Exit', callback_data='exit'), InlineKeyboardButton("Main Menu", callback_data="main")]]
    return InlineKeyboardMarkup(keyboard)

def group_serivce_billpay_menu_keyboard():
    list_group_service = ["water", "telecom", "school", "evn", "hcc", "hospital", "apartment"]
    keyboard = []
    keyboard_side_by_side = []
    for service in list_group_service:
        obj = InlineKeyboardButton("{}".format(service.upper()), callback_data="{}".format(service))
        keyboard_side_by_side.append(obj)
        if len(keyboard_side_by_side) < 2:
            continue
        else:
            keyboard.append(keyboard_side_by_side)
            keyboard_side_by_side = []
    keyboard.append([InlineKeyboardButton('Exit', callback_data='exit'), InlineKeyboardButton("Main Menu", callback_data="main")])
    return InlineKeyboardMarkup(keyboard)

def list_serivce_billpay_menu_keyboard(group_service):
    keyboard = []
    keyboard_side_by_side = []
    if group_service == 'water':
        list_service =  ['kimlien_water', 'nuocbenthanh', 'nuocnongthon', 'kimlien_water', 'nuocbenthanh', 'nuocnongthon']
        for service in list_service:
            obj = InlineKeyboardButton("{}".format(service), callback_data="{}".format(service))
            keyboard_side_by_side.append(obj)
            if len(keyboard_side_by_side) < 3:
                continue
            else:
                keyboard.append(keyboard_side_by_side)
                keyboard_side_by_side = []
        # print(keyboard)        
        keyboard.append([InlineKeyboardButton('Exit', callback_data='exit'), InlineKeyboardButton("Main Menu", callback_data="main")])
    return InlineKeyboardMarkup(keyboard)

def check_service(service):

    pass

def menu_telco_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def exit_menu_keyboard():
    keyboard = []
    return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

############################# Handlers #########################################
updater = Updater('5181574497:AAECXpM8JLPFYtjHpp_Tx0CnVvdHvIF1C-Y', use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))

# Main Menu
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(billpay_menu, pattern='billpay'))
updater.dispatcher.add_handler(CallbackQueryHandler(telco_menu, pattern='telco'))
updater.dispatcher.add_handler(CallbackQueryHandler(exit_menu, pattern='exit'))

# Group Service Menu Billpay
updater.dispatcher.add_handler(CallbackQueryHandler(check_service_billpay_maintain, pattern='check'))
list_group_service = ["water", "telecom", "school", "evn", "hcc", "hospital", "apartment", "main"]
for service in list_group_service:
    updater.dispatcher.add_handler(CallbackQueryHandler(list_service_and_check, pattern=service))

# Print Error Log
updater.dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()
################################################################################