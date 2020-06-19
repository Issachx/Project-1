import telebot
from selenium import webdriver
import win32com.client as wincl
from shutdown import *
import time
#Variabel menampung Token
name = 'Isaac bot'
TOKEN ='1247250466:AAFRtuss4Qgn0qCffZ2Txmg7MygBFWMmyLY'
isaachx_bot = telebot.TeleBot(token=TOKEN)


def talking():
    speak = wincl.Dispatch('SAPI.Spvoice')
    speak.Speak('Welcome to isaac bot how can i help for you')
    isaachx_bot.send_message(chat_id=1014061753, text='Halo selamat datang di isaachx_bot apa yang kamu cari?\n'
                                                      'ketik : /start')



@isaachx_bot.message_handler(commands=['start'])
def send_welcome(message):
    isaachx_bot.reply_to(message,'Daftar Remote : \n'
                                 '1.Open google :/1 \n'
                                 '2.Open youtube :/2 \n'
                                 '3.shutdown /3')

@isaachx_bot.message_handler(commands=['1'])
def open_google(message):
    isaachx_bot.reply_to(message,'opening google')
    browser = webdriver.Firefox(executable_path='C:/FIREFOX_DRIVER/geckodriver.exe')
    # Searching youtube
    browser.get('https://www.google.com/')

@isaachx_bot.message_handler(commands=['2'])
def open_yt(message):
    isaachx_bot.reply_to(message,'opening yt')
    browser = webdriver.Firefox(executable_path='C:/FIREFOX_DRIVER/geckodriver.exe')
    # Searching youtube
    browser.get('https://www.google.com/')

@isaachx_bot.message_handler(commands=['3'])
def stdwn(message):
    isaachx_bot.reply_to(message, 'computer shutdown in :')
    for x in reversed(range(10)):
        isaachx_bot.reply_to(message,x)
        time.sleep(1)
        if x == 0:
            shutdown()




talking()
print('Bot start running')
isaachx_bot.polling()
