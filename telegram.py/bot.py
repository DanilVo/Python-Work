import datetime
import random

import pandas_datareader as web
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

# def log(update: Update, context: CallbackContext):
#     file = open('info.csv', 'a')
#     file.write(f'{update.effective_user.first_name} , {update.effective_user.id} ')
#     file.close()


def stock(update, contex):
    ticker = contex.args[0]
    data = web.DataReader(ticker, 'google')
    price = data.ilock[-1]['Close']
    update.message.reply_text(
        f'the current price of {ticker} is {price:.2f}$!')


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def date_time(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def game(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(msg)
    update.message.reply_text('Roll The Dice!')
    update.message.reply_text(f'dice 1: {random.randint(1,7)}')
    update.message.reply_text(f'dice 2: {random.randint(1,7)}')
    update.message.reply_text('\nDo you want to roll again?\nYes: 1\nNo: 2\n')


def continue_game(update: Update, context: CallbackContext):
    msg = update.message.text
    # update.message.reply_text(msg)
    update.message.reply_text(f'Dice 1: {random.randint(1,7)}')
    update.message.reply_text(f'Dice 2: {random.randint(1,7)}')
    update.message.reply_text('\nDo you want to roll again?\nYes: 1\nNo: 2\n')


def finish_game(update: Update, context: CallbackContext):
    msg = update.message.text
    # update.message.reply_text(msg)
    update.message.reply_text('Have a good day!')


def link(update: Update, context: CallbackContext):
    update.message.reply_html('https://www.google.co.il/')


updater = Updater('5238378094:AAFIm2TQxotUuThPD6nzq2YLmIS2_7Pj6XI')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('game', game))

updater.dispatcher.add_handler(CommandHandler('1', continue_game))

updater.dispatcher.add_handler(CommandHandler('2', finish_game))

updater.dispatcher.add_handler(CommandHandler('time', date_time))

updater.dispatcher.add_handler(CommandHandler('google', link))

updater.dispatcher.add_handler(CommandHandler('stock', stock))


print(datetime.datetime.now())
print('server up')
updater.start_polling()
updater.idle()


# separated the original code as i could not use (input) in order to say coomad what to do next step

# updater.dispatcher.add_handler(CommandHandler('hello', hello)) - set a coonad as first iterriable and uses function as second iterriable

# update.message.reply_text - text that will be shown to a user
