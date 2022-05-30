import telebot
from telebot import types
from api_key import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode="html")


@bot.message_handler(commands=['start'])
def start(message, res=False):
    mes = f"Привет, {message.from_user.first_name}! Я помощник экоклуба СЭИ :)"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📒мероприятия")
    item2 = types.KeyboardButton("☎контакты")
    item3 = types.KeyboardButton("📝поиск статей")
    item4 = types.KeyboardButton("другое")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, mes, reply_markup=markup)


@bot.message_handler(content_types='text')
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "📒мероприятия":
            m_digest = 'Вот расписание мероприятий на ближайшую неделю:'
            bot.send_message(message.chat.id, m_digest)

        elif message.text == "☎контакты":
            m_contact_people = "Вот контакты главы экоклуба Евы: <a href='https://vk.com/evalutionn'>VK</a>, " \
                               " <a href='tg://@evanaza'>Telegram</a>\n" \
                               "А это ссылка на экоклуб: <a href='https://t.me/+kLQAtgkIZ5FlZDgy'>SEI</a>"
            bot.send_message(message.chat.id, m_contact_people)

        elif message.text == "📝поиск статей":
            m_articles = "эта функция все еще в разработке :),\nно вот наш вк со лонгридами: " \
                         "<a href='https://vk.com/sei_club_iss_ranepa'>SEI</a>"
            bot.send_message(message.chat.id, m_articles)
        elif message.text == "другое":
            m_else_f = 'Я постараюсь помочь с любым запросом, поэтому напиши, что именно ты ищешь'
            bot.send_message(message.chat.id, m_else_f)

bot.polling(none_stop=True, interval=0)
