from requests import get
from telebot import TeleBot
from const import * # Тут храню токены и другие константы
import json


bot = TeleBot(token)


@bot.message_handler(commands)
def send_welcome(message):
    bot.send_message(
     message.from_user.id, "В каком городе тебе интересна погода?")
    ''' bot.reply_to(message, "В каком городе тебе интересна погода?") '''


@bot.message_handler(content_types)
def handle_text(message):
    ans_from_owm = get(base_url + message.text + lang + appid).text
    '''Запрос в api OpenWeatherMap'''
    weather = json.loads(ans_from_owm)
    print(weather)
    try:
        bot.send_message(
         message.from_user.id,
         'Широта: ' + str(weather['coord']['lon']) + '\n' +
         'Долгота: ' + str(weather['coord']['lat']) + '\n' +
         'Погода: ' + str(weather['weather'][0]['description']) + '\n' +
         'Температура: ' + str(round(weather['main']['temp'] - 273)) + '\n' +
         'Скорость ветра: ' + str(weather['wind']['speed']) + ' м/с')
    except Exception:
        bot.send_message(
         message.from_user.id,
         'Город не найден, попробуйте ввести в другом формате')


print(bot.get_me())
bot.polling(none_stop=True)
