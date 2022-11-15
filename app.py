import telebot
import config

#TOKEN = "5625506966:AAGvXbDhv8dMBmkpGSdWZFEtRMxnCu1VD3E"

#keys = {
#    'рубль': 'RUB',
#    'евро': 'EUR',
#    'доллар': 'USD',
#}

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n <имя валюты цену которой хотите узнать> \
<имя валюты в которой надо узнать цену первой валюты> \
<количество переводимой валюты> \n Увидеть список всех доступных валют: /values'

    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):


bot.polling()