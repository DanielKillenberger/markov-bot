import markovify
import json
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
path = 'models/'
model_string = str(sys.argv[1])
suffix = '_model.json'

credentials = open('credentials.json').read()
credentials = json.loads(credentials)
telegram_token = credentials['telegram_api_token']
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# load model from file
with open(path + model_string + suffix) as model_file:
    model = markovify.Text.from_json(json.load(model_file))


def schnur(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=model.make_sentence())


start_handler = CommandHandler('schnur', schnur)
dispatcher.add_handler(start_handler)

updater.start_polling()

