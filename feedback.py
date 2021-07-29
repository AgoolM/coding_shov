from transliterate import to_cyrillic, to_latin
import telebot



TOKEN = "" #<-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """ Start komandasiga javob beradi """
    username = message.from_user.username
    xabar = f'Assalom alaykum, {username}, Menga xabaringizni yo\'llashingiz mumkin!'
    bot.reply_to(message, xabar)


@bot.message_handler(func=lambda msg: msg.from_user.id!=1056874967)
def admingajonat(message):
    """ Bu funksiya adminga jo'natadi """
    print('birinchisi')
    msg = message.text
    from_chat_id = message.from_user.id
    message_id = message.message_id
    bot.forward_message(1056874967, from_chat_id, message_id)


def tekshir(msg):
    replymi = 'reply_to_message' in msg.json
    return msg.from_user.id==1056874967 and replymi

@bot.message_handler(func=lambda x: tekshir(x))
def usergajonatadi(message):
    """ Bu funksiya userga jo'natadi """
    print('ikkinchisi')
    msg = message.text
    from_chat_id = 1056874967
    to_chat_id = message.json['reply_to_message']['forward_from']['id']
    print(message.json)
    message_id = message.message_id
    bot.forward_message(to_chat_id, from_chat_id, message_id)


bot.polling()
