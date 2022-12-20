import telegram

TELEGRAM_BOT_TOKEN = '5026185888:AAGuZmrT4R4unv-F_f5Yj_v7nH32-RXdRaw'
TELEGRAM_CHAT_ID = '-725471006'
PHOTO_PATH = 'phatbui.png'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Telegram Bot")

bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))

dict = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}
buttons = []

for key, value in dict.items():
    buttons.append(
    [InlineKeyboardButton(text = key, url = 'google.com')]
    )
keyboard = InlineKeyboardMarkup(buttons)
bot.sendMessage(TELEGRAM_CHAT_ID,text = 'f', reply_markup = keyboard)