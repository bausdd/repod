from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from twilio.twiml.voice_response import VoiceResponse, Gather, Play, Hangup
from twilio.rest import Client
from flask import Flask, request
import cmd
import signal
import time
import os
from call import viker

updater = Updater("5340638171:AAHGlF78oNj9DesADBODkztjdFBbhKOG1nk",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to reelur otp do /help to see commands")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""---Reelur OTP Commands---
    /call -6 or 7 digit otp
    /cvv - To get cvv of card
    /cancel -  Cancel any action""")


def makecall():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']='ACeb56770731e88aa403413041a537144d'
    auth_token = os.environ['TWILIO_AUTH_TOKEN']='15252c0f69c2e6e979d7cd4b3c0409f9'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                        url='http://kdhdh.pythonanywhere.com',
                        to='+19495709965',
                        from_='+19377708941',
                                    
            )
    

def call(update: Update, context: CallbackContext):
    update.message.reply_text("wait")
    makecall()

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Action Canceled!")
    

def cvv(update: Update, context: CallbackContext):
    update.message.reply_text("Y")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "'%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cvv', cvv))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('call', call))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
