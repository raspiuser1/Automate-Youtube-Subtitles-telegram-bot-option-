from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import datetime
import random
import os
import subs
import time
import convert
from subs import *


#auto wait 
subs.autodelay = 1
subs.woord = 0.5 #sleeptime per word

#sleeptime after complete sentence with a dot(.)
subs.zinsec = 5

#start time first sub (max 59 sec)
subs.starttijd = 2



#credits @ rob226@gmail.com
#token that can be generated talking with @BotFather on telegram, put this in key.txt
my_token=open("key.txt").readline().rstrip()
#store plain txt in:
txtfile = ""


updater = Updater(my_token,use_context=True)
bot = telegram.Bot(token=my_token)

def help(update: Update, context: CallbackContext):
	update.message.reply_text(""" ===Options YT subtitle Bot===
Credits @ https://github.com/raspiuser1

/sustart - paste plain text which needs\n to be translated, multiple msges are possible.

/app - append to existing config, you can use it after /tra

/sustop - stops listening for plain text\nyou need to start again with /sustart

/tra [videoname]- translate pasted text \nand the youtube sub will be send to you, you can append using /app or /sustart for a fresh start

/show - show current timings

/tim [w] [z] [s] - adapt timings \n[w]=readtime in sec per word(def=0.5)\n[z]=sleeptime in sec after sentence\n[s]=starttime first sub (max 59sec)
""")
    
start = 0
tekst = ""

def boot(update: Update, context: CallbackContext):
    update.message.reply_text("Subtitle bot started")


def sustart(update: Update, context: CallbackContext):
    update.message.reply_text("Starting to listen for plain text")
    global start
    global tekst
    global txtfile
    val2 = randomnu()
    txtfile = "telegram_" + val2 + ".txt"
    start = 1
    tekst = ""

def app(update: Update, context: CallbackContext):
    update.message.reply_text("Appending to existing config, listening for plain text")
    global start
    start = 1

def tim(update: Update, context: CallbackContext):
    try:
        wt = update.message.text.split(" ")
        subs.woord = float(wt[1])
        subs.zinsec = int(wt[2])
        subs.starttijd = int(wt[3])
        if subs.starttijd > 59:
            subs.starttijd = 59
            update.message.reply_text("Starttime first sub adapted to max 59 sec")
        values()    
        update.message.reply_text(waarden)
    except:
        update.message.reply_text("Error: Fill in all the arguments")
    
    
def show(update: Update, context: CallbackContext):
    values()
    update.message.reply_text(waarden)
    
    
def values():
    global waarden
    waarden = "===Current timings===\nWait time per word: " + str(subs.woord) + " sec\n"\
    "Sleeptime after sentence with dot(.): " + str(subs.zinsec) + " sec\n"\
    "Start time first sub at: " + str(subs.starttijd) + " sec\n"

    
def sustop(update: Update, context: CallbackContext):
    update.message.reply_text("Stop listening for plain text")
    global start
    global tekst
    start = 0
    tekst = ""

def txt(update: Update, context: CallbackContext):
        global tekst
        tekst += update.message.text + " "

def randomnu():
	randnu7 = str(random.randint(1, 100)) + str(random.randint(1, 100))  + str(random.randint(1, 100))
	return randnu7

def tra(update: Update, context: CallbackContext):
    global directory
    global fname4
    global fname5
    global start
    chat_id = update.message.chat_id	
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    userinfo = ("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))

    if start == 0 :
        update.message.reply_text("Use /sustart first")
        return
    try:
        wt = update.message.text.split(" ")
        directory = str(wt[1])
        fname4 = 1
    except:
        val2 = randomnu()
        directory = "telegram" + val2 + "_" + str(datetime.date.today())
        fname4 = 0
        
    update.message.reply_text("Translating plain text to english")
    with open(txtfile, 'w') as f:
         f.write(tekst)
    translate(txtfile,directory)
 
    duration = subs.val2
    values()
    update.message.reply_text(waarden)
    update.message.reply_text("Translating and subbing is done, Upload this file in Youtube studio with timing enabled, Make sure"\
                                      "the video is not longer then " + str(duration) + " or change the timing")

    with open(directory + "/userinfo.txt", 'w') as f:
         f.write(userinfo)
    try:              
            os.remove(subs.file9)
    except:
            print("cannot delete " + subs.file9)


    try:
            os.popen('mv ' + convert.file4 + " "  + directory  + "/converted.txt")
    except:
            print("cannot move " + convert.file4)

    if fname4 == 1:
                try:
                    os.popen('cp ' + directory + "/captions.txt "  + directory  + "/" + directory + ".txt")
                    time.sleep(0.5)
                    os.remove(directory + "/captions.txt")
                    fname5 = directory   
                except:
                    print("cannot copy captions.txt")
                    fname5 = "captions"
    else:
                    fname5 = "captions"

        #must sleep before sending file
    time.sleep(1)

    try:    
            with open(directory + "/" + fname5 + ".txt", 'rb') as f:
                  chat_id1=update.effective_chat.id
                  bot.sendDocument(chat_id1,f)
            time.sleep(1)
    except :
            update.message.reply_text("Unable to transfer file")

    
    
def unknown_text(update: Update, context: CallbackContext):
    #uncomment if need to send to telegram:
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    print("Sorry I can't recognize you , you said '%s'")

def main():
    #telegram options=================================================================================================
    updater.dispatcher.add_handler(CommandHandler('suhelp', help))
    updater.dispatcher.add_handler(CommandHandler('sustart', sustart))
    updater.dispatcher.add_handler(CommandHandler('sustop', sustop))
    updater.dispatcher.add_handler(CommandHandler('app', app))
    updater.dispatcher.add_handler(CommandHandler('tim', tim))
    updater.dispatcher.add_handler(CommandHandler('show', show))
    updater.dispatcher.add_handler(CommandHandler('tra', tra)) 
    updater.dispatcher.add_handler(MessageHandler(Filters.text, txt))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, txt)) # Filters out unknown commands
        # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    updater.start_polling()
    
main()    
