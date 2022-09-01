import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types

book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

bot = telebot.TeleBot('5597120964:AAHu9iHjb1tsIbHYwmlvQ-a0cdXnkXUpwD8')

def sp19(message):
	para1 = sheet["AY2"].value
	paracab1 = sheet["AZ2"].value
	para2 = sheet["AY3"].value
	paracab2 = sheet["AZ3"].value
	para3 = sheet["AY4"].value
	paracab3 = sheet["AZ4"].value
	para4 = sheet["AY5"].value
	paracab4 = sheet["AZ5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `СП-19`: 
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def at2_29(message):
	para1 = sheet["BA2"].value
	paracab1 = sheet["BB2"].value
	para2 = sheet["BA3"].value
	paracab2 = sheet["BB3"].value
	para3 = sheet["BA4"].value
	paracab3 = sheet["BB4"].value
	para4 = sheet["BA5"].value
	paracab4 = sheet["BB5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `2АТ-19`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')