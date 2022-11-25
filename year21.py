import openpyxl
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
from telebot import types
from config import token
book = openpyxl.open("data.xlsx", read_only=True)
sheet = book.active

bot = telebot.TeleBot(token)

#QR ST UV WX YZ AAAB ACAD AEAF

def mroa21(message):
	para1 = sheet["Q2"].value
	paracab1 = sheet["R2"].value
	para2 = sheet["Q3"].value
	paracab2 = sheet["R3"].value
	para3 = sheet["Q4"].value
	paracab3 = sheet["R4"].value
	para4 = sheet["Q5"].value
	paracab4 = sheet["R5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МРОА-21`: 
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
def s21(message):
	para1 = sheet["S2"].value
	paracab1 = sheet["T2"].value
	para2 = sheet["S3"].value
	paracab2 = sheet["T3"].value
	para3 = sheet["S4"].value
	paracab3 = sheet["T4"].value
	para4 = sheet["S5"].value
	paracab4 = sheet["T5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `С-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def t21(message):
	para1 = sheet["U2"].value
	paracab1 = sheet["V2"].value
	para2 = sheet["U3"].value
	paracab2 = sheet["V3"].value
	para3 = sheet["U4"].value
	paracab3 = sheet["V4"].value
	para4 = sheet["U5"].value
	paracab4 = sheet["V5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `Т-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def mjkh21(message):
	para1 = sheet["W2"].value
	paracab1 = sheet["X2"].value
	para2 = sheet["W3"].value
	paracab2 = sheet["X3"].value
	para3 = sheet["W4"].value
	paracab3 = sheet["X4"].value
	para4 = sheet["W5"].value
	paracab4 = sheet["X5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЖКХ-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def mci21(message):
	para1 = sheet["Y2"].value
	paracab1 = sheet["Z2"].value
	para2 = sheet["Y3"].value
	paracab2 = sheet["Z3"].value
	para3 = sheet["Y4"].value
	paracab3 = sheet["Z4"].value
	para4 = sheet["Y5"].value
	paracab4 = sheet["Z5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `МЦИ-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def at2_21(message):
	para1 = sheet["AA2"].value
	paracab1 = sheet["AB2"].value
	para2 = sheet["AA3"].value
	paracab2 = sheet["AB3"].value
	para3 = sheet["AA4"].value
	paracab3 = sheet["AB4"].value
	para4 = sheet["AA5"].value
	paracab4 = sheet["AB5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `2АТ-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def sp21(message):
	para1 = sheet["AC2"].value
	paracab1 = sheet["AD2"].value
	para2 = sheet["AC3"].value
	paracab2 = sheet["AD3"].value
	para3 = sheet["AC4"].value
	paracab3 = sheet["AD4"].value
	para4 = sheet["AC5"].value
	paracab4 = sheet["AD5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `СП-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
#QR ST UV WX YZ AAAB ACAD AEAF
def k21(message):
	para1 = sheet["AE2"].value
	paracab1 = sheet["AF2"].value
	para2 = sheet["AE3"].value
	paracab2 = sheet["AF3"].value
	para3 = sheet["AE4"].value
	paracab3 = sheet["AF4"].value
	para4 = sheet["AE5"].value
	paracab4 = sheet["AF5"].value
	bot.send_message(message.chat.id, f'''*Расписание на сегодня для группы* `К-21`:
		*1.* {para1} - `{paracab1}`
		*2.* {para2} - `{paracab2}`
		*3.* {para3} - `{paracab3}`
		*4.* {para4} - `{paracab4}`''', parse_mode='Markdown')
