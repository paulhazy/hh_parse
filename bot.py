import telebot

token = '1207237270:AAGVTkfKAbjjBGP_D8N7-LZ6EIUSPZVca48'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat(msg):
    bot.send_message(msg.chat.id, msg.text)

if __name__ == '__main__':
    bot.infinity_polling()