import telebot
import wikipedia
wikipedia.set_lang("uz")
bot=telebot.TeleBot("6584502500:AAGhLNjMaiqSamjaOn7JYjp90OMW3NLLJhQ")
@bot.message_handler(commands=['sart'])
def start(message):
    bot.send_message(message.chat.id,'salom')
@bot.message_handler(content_types=["text"])
def text(message):
    final=message.text
    try:
        mess=wikipedia.summary(final)

        bot.send_message(message.chat.id,mess)


    except:
        bot.send_message(message.chat.id,"Error")
bot.polling()