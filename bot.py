import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types
from year19 import *
from year20 import *
from year21 import *
from year22 import *
from config import token
print("""Охаё, семпай)""")
print("""Приступаю к работе""")
########################################################################
bot = telebot.TeleBot(token)#
########################################################################
book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

@bot.message_handler(commands=['start'])
def start(message):
	keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
	sp19 = types.KeyboardButton("СП-19")
	at2_19 = types.KeyboardButton("2АТ-19")
	keyboard.row(sp19, at2_19)
	mroa20 = types.KeyboardButton("МРОА-20")
	s20 = types.KeyboardButton("С-20")
	t20 = types.KeyboardButton("Т-20")
	mjkh20 = types.KeyboardButton("МЖКХ-20")
	keyboard.row(mroa20, s20, t20, mjkh20)
	mci20 = types.KeyboardButton("МЦИ-20")
	at2_20 = types.KeyboardButton("2АТ-20")
	sp20 = types.KeyboardButton("СП-20")
	keyboard.row(mci20, at2_20, sp20)
	mroa21 = types.KeyboardButton("МРОА-21")
	s21 = types.KeyboardButton("С-21")
	t21 = types.KeyboardButton("Т-21")
	mjkh21 = types.KeyboardButton("МЖКХ-21")
	keyboard.row(mroa21, s21, t21, mjkh21)
	mci21 = types.KeyboardButton("МЦИ-21")
	at2_21 = types.KeyboardButton("2АТ-21")
	sp21 = types.KeyboardButton("СП-21")
	k21 = types.KeyboardButton("К-21")
	keyboard.row(mci21, at2_21, sp21, k21)
	mroa22 = types.KeyboardButton("МРОА-22")
	s22 = types.KeyboardButton("С-22")
	t22 = types.KeyboardButton("Т-22")
	mjkh22 = types.KeyboardButton("2МРОА-22")
	keyboard.row(mroa22, s22, t22, mjkh22)
	mci22 = types.KeyboardButton("МЦИ-22")
	at2_22 = types.KeyboardButton("2АТ-22")
	sp22 = types.KeyboardButton("СП-22")
	k22 = types.KeyboardButton("К-22")
	keyboard.row(mci22, at2_22, sp22, k22)
	rzh22 = types.KeyboardButton("РЗХ-22")
	keyboard.row(rzh22)
	mainmessage = '''Приветик) Меня зовут *Распи*. Я подскажу тебе расписание твоих пар на сегодня в твоём любимом Копейском Политехническом.)
	
	Выбирай свою группу. Удачного дня, семпай)
	'''
	photo = open('photomes.jpg', 'rb')
	mainmesage = bot.send_photo(message.chat.id, photo, caption=mainmessage, parse_mode="Markdown", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def mainfunction(message):
	if message.text == 'СП-19':
		sp19(message)
	if message.text == '2АТ-19':
		at2_19(message)
	if message.text == 'МРОА-20':
		mroa20(message)
	if message.text == 'С-20':
		s20(message)
	if message.text == 'Т-20':	
		t20(message)
	if message.text == 'МЦИ-20':	
		mci20(message)
	if message.text == '2АТ-20':	
		at2_20(message)
	if message.text == 'СП-20':	
		sp20(message)
	if message.text == 'МЖКХ-20':
		mjkh20(message)
	if message.text == 'МРОА-21':
		mroa21(message)
	if message.text == 'С-21':
		s21(message)
	if message.text == 'Т-21':	
		t21(message)
	if message.text == 'МЦИ-21':	
		mci21(message)
	if message.text == '2АТ-21':	
		at2_21(message)
	if message.text == 'СП-21':	
		sp21(message)
	if message.text == 'МЖКХ-21':
		mjkh21(message)
	if message.text == 'К-21':	
		k21(message)
	if message.text == 'МРОА-22':
		mroa22(message)
	if message.text == 'С-22':
		s22(message)
	if message.text == 'Т-22':	
		t22(message)
	if message.text == 'МЦИ-22':	
		mci22(message)
	if message.text == '2АТ-22':	
		at2_22(message)
	if message.text == 'СП-22':	
		sp22(message)
	if message.text == '2МРОА-22':
		mjkh22(message)
	if message.text == 'К-22':	
		k22(message)
	if message.text == "РЗХ-22":
		rzh22(message)

	# else:
	# 	bot.send_message(message.chat.id, text="Произошла какая-то ошибка :( попробуй еще раз, пожалуйста")


@bot.message_handler(commands=['author'])
def author(message):
	photo = open('authorphoto.jpg', "rb")
	authormessage = """*Ого*, тебя заинтересовала информация о моём создателе, ну тогда *слушай*.
	Меня создал один очень талантливый программист [Sai](@saikonohack). Он создавал и *создаёт* моих братиков и сестричек ботов)
	
	Все мы ооочень разные. Один, например, жутко любит следить за *ставками* на *футбол*. Другой *консультирует* людей *при поездках* в зарубежные страны
	Ты тоже можешь попросить сделать себе бота, и он *обязательно тебе поможет*)
	"""
	bot.send_photo(message.chat.id, photo, caption=authormessage, parse_mode='Markdown',reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['help'])
def help(message):
	pass
@bot.message_handler(commands=['call'])
def call(message):
	bot.send_message(message.chat.id, text="""*Расписание звонков*
		1) 8:00 - 8:45, 8:55 - 9:40
		2) 9:50 - 10:30, 10:55 - 11:40
		3) 12:00 - 12:45, 12:55 - 13:40
		4) 13:50 - 14:35, 14:45 - 15:30
		""", parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
try:
    bot.polling(none_stop=True)
except Exception as e:
    logger.exception("Fail startup:", e)
