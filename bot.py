import telebot

token = '###################'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat(msg):
    bot.send_message(msg.chat.id, msg.text)

if __name__ == '__main__':
    bot.infinity_polling()
