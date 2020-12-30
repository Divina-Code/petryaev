import telebot

bot = telebot.TeleBot('1362891506:AAEsh6hGWypbbxpDUO-6jULCrLGwkCnpjDU')  #создаем подключение к боту


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, 'shut up')




bot.polling()  #забираем сообщения у бота

