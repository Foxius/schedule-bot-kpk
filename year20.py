import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types

book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

bot = telebot.TeleBot('5597120964:AAHu9iHjb1tsIbHYwmlvQ-a0cdXnkXUpwD8')

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
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
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
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
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
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
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
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def mci20(message):
	para1 = sheet["I2"].value
	paracab1 = sheet["J2"].value
	para2 = sheet["I3"].value
	paracab2 = sheet["J3"].value
	para3 = sheet["I4"].value
	paracab3 = sheet["J4"].value
	para4 = sheet["I5"].value
	paracab4 = sheet["J5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЦИ-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def at2_20(message):
	para1 = sheet["K2"].value
	paracab1 = sheet["L2"].value
	para2 = sheet["K3"].value
	paracab2 = sheet["L3"].value
	para3 = sheet["K4"].value
	paracab3 = sheet["L4"].value
	para4 = sheet["K5"].value
	paracab4 = sheet["L5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `2АТ-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def sp20(message):
	para1 = sheet["M2"].value
	paracab1 = sheet["N2"].value
	para2 = sheet["M3"].value
	paracab2 = sheet["N3"].value
	para3 = sheet["M4"].value
	paracab3 = sheet["N4"].value
	para4 = sheet["M5"].value
	paracab4 = sheet["N5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `СП-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def k20(message):
	para1 = sheet["O2"].value
	paracab1 = sheet["P2"].value
	para2 = sheet["O3"].value
	paracab2 = sheet["P3"].value
	para3 = sheet["O4"].value
	paracab3 = sheet["P4"].value
	para4 = sheet["O5"].value
	paracab4 = sheet["P5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `К-20`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')