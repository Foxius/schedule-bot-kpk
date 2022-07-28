import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types

print("""Доброе утро, семпай)""")
print("""Приступаю к работе""")

bot = telebot.TeleBot('5597120964:AAEyTnVfB4wj-mL1ekygTCDnUygJ_MXEhNQ')
book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

@bot.message_handler(commands=['start'])
def start(message):
	keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn = types.KeyboardButton("МРОА-20")
	keyboard.add(btn)
	btn1 = types.KeyboardButton("С-20")
	keyboard.add(btn1)
	btn2 = types.KeyboardButton("Т-20")
	keyboard.add(btn2)
	btn3 = types.KeyboardButton("МЖКХ-20")
	keyboard.add(btn3)
	mainmessage = '''Приветик) Меня зовут *Распи*. Я подскажу тебе расписание твоих пар на сегодня в твоём любимом Копейском Политехническом.)
	
	Чтобы я тебе помогала и дальше, запомни: Перед получением расписания *ОБЯЗАТЕЛЬНО* поздоровайся со мной при помощи команды /start
	
	И только после этого выбирай свою группу. Удачного дня, семпай)
	'''
	photo = open('photomes.jpg', 'rb')
	mainmesage = bot.send_photo(message.chat.id, photo, caption=mainmessage, parse_mode="Markdown", reply_markup=keyboard)
	bot.register_next_step_handler(mainmesage,mainfunction)


def mainfunction(message):
	if message.text == 'МРОА-20':
		mroa20(message)
	if message.text == 'С-20':
		s20(message)
	if message.text == 'Т-20':	
		t20(message)
	if message.text == 'МЖКХ-20':	
		mjkh20(message)	
	else:
		bot.send_message(message.chat.id, text="Произошла какая-то ошибка :( попробуй еще раз, пожалуйста")

def mroa20(message):
	para1 = sheet["A2"].value
	paracab1 = sheet["B2"].value
	para2 = sheet["A3"].value
	paracab2 = sheet["B3"].value
	para3 = sheet["A4"].value
	paracab3 = sheet["B4"].value
	para4 = sheet["A5"].value
	paracab4 = sheet["B5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МРОА-20`: 
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())

def s20(message):
	para1 = sheet["C2"].value
	paracab1 = sheet["D2"].value
	para2 = sheet["C3"].value
	paracab2 = sheet["D3"].value
	para3 = sheet["C4"].value
	paracab3 = sheet["D4"].value
	para4 = sheet["C5"].value
	paracab4 = sheet["D5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `С-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())

def t20(message):
	para1 = sheet["E2"].value
	paracab1 = sheet["F2"].value
	para2 = sheet["E3"].value
	paracab2 = sheet["F3"].value
	para3 = sheet["E4"].value
	paracab3 = sheet["F4"].value
	para4 = sheet["E5"].value
	paracab4 = sheet["F5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `Т-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())

def mjkh20(message):
	para1 = sheet["G2"].value
	paracab1 = sheet["H2"].value
	para2 = sheet["G3"].value
	paracab2 = sheet["H3"].value
	para3 = sheet["G4"].value
	paracab3 = sheet["H4"].value
	para4 = sheet["G5"].value
	paracab4 = sheet["H5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЖКХ-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())













@bot.message_handler(commands=['author'])
def author(message):
	photo = open('authorphoto.jpg', "rb")
	authormessage = """*Ого*, тебя заинтересовала информация о моём создателе, ну тогда *слушай*.
	Меня создал один очень талантливый программист [Sai](@saikonohack). Он создавал и *создаёт* моих братиков и сестричек ботов)
	
	Все мы ооочень разные. Один, например, жутко любит следить за *ставками* на *футбол*. Другой *консультирует* людей *при поездках* в зарубежные страны
	Ты тоже можешь попросить сделать себе бота, и он *обязательно тебе поможет*)
	"""
	bot.send_photo(message.chat.id, photo, caption=authormessage, parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True, interval=0)
try:
    bot.polling(none_stop=True)
except Exception as e:
    logger.exception("Fail startup:", e)


# print(sheet["B2"].value)