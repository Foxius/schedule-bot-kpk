import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types

book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

bot = telebot.TeleBot('5597120964:AAHu9iHjb1tsIbHYwmlvQ-a0cdXnkXUpwD8')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def mroa22(message):
	para1 = sheet["AG2"].value
	paracab1 = sheet["AH2"].value
	para2 = sheet["AG3"].value
	paracab2 = sheet["AH3"].value
	para3 = sheet["AG4"].value
	paracab3 = sheet["AH4"].value
	para4 = sheet["AG5"].value
	paracab4 = sheet["AH5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МРОА-22`: 
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def s22(message):
	para1 = sheet["AI2"].value
	paracab1 = sheet["AJ2"].value
	para2 = sheet["AI3"].value
	paracab2 = sheet["AJ3"].value
	para3 = sheet["AI4"].value
	paracab3 = sheet["AJ4"].value
	para4 = sheet["AI5"].value
	paracab4 = sheet["AJ5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `С-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AKAL AMAN AOAP AQAR ASAT AUAV
def t22(message):
	para1 = sheet["AK2"].value
	paracab1 = sheet["AL2"].value
	para2 = sheet["AK3"].value
	paracab2 = sheet["AL3"].value
	para3 = sheet["AK4"].value
	paracab3 = sheet["AL4"].value
	para4 = sheet["AK5"].value
	paracab4 = sheet["AL5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `Т-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def mjkh22(message):
	para1 = sheet["AM2"].value
	paracab1 = sheet["AN2"].value
	para2 = sheet["AM3"].value
	paracab2 = sheet["AN3"].value
	para3 = sheet["AM4"].value
	paracab3 = sheet["AN4"].value
	para4 = sheet["AM5"].value
	paracab4 = sheet["AN5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЖКХ-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def mci22(message):
	para1 = sheet["AO2"].value
	paracab1 = sheet["AP2"].value
	para2 = sheet["AO3"].value
	paracab2 = sheet["AP3"].value
	para3 = sheet["AO4"].value
	paracab3 = sheet["AP4"].value
	para4 = sheet["AO5"].value
	paracab4 = sheet["AP5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЦИ-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def at2_22(message):
	para1 = sheet["AQ2"].value
	paracab1 = sheet["AR2"].value
	para2 = sheet["AQ3"].value
	paracab2 = sheet["AR3"].value
	para3 = sheet["AQ4"].value
	paracab3 = sheet["AR4"].value
	para4 = sheet["AQ5"].value
	paracab4 = sheet["AR5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `2АТ-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def sp22(message):
	para1 = sheet["AS2"].value
	paracab1 = sheet["AT2"].value
	para2 = sheet["AS3"].value
	paracab2 = sheet["AT3"].value
	para3 = sheet["AS4"].value
	paracab3 = sheet["AT4"].value
	para4 = sheet["AS5"].value
	paracab4 = sheet["AT5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `СП-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#AGAH AIAJ AKAL AMAN AOAP AQAR ASAT AUAV
def k22(message):
	para1 = sheet["AU2"].value
	paracab1 = sheet["AV2"].value
	para2 = sheet["AU3"].value
	paracab2 = sheet["AV3"].value
	para3 = sheet["AU4"].value
	paracab3 = sheet["AV4"].value
	para4 = sheet["AU5"].value
	paracab4 = sheet["AV5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `К-22`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')