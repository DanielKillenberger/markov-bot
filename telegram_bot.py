import os

import markovify
import json
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging


path = 'models/'
suffix = '_model.json'


def main():
    if len(sys.argv) != 2:
        print('Give model name as program argument - e.g if file is called test_model.json give "test" as argument.')
        return

    model_string = str(sys.argv[1])
    model_file_path = path + model_string + suffix
    if not os.path.isfile(model_file_path):
        print('No model at {model_file_path}'.format(**locals()))
        return

    config = open('config.json').read()
    config = json.loads(config)

    telegram_token = config['token']
    updater = Updater(token=telegram_token)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # load model from file
    with open(path + model_string + suffix) as model_file:
        model = markovify.Text.from_json(json.load(model_file))

    def talk(bot, update):
        answer = None
        while answer is None:
            answer = model.make_sentence(tries=100)
        bot.sendMessage(chat_id=update.message.chat_id, text=answer)

    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=config['start_answer'])

    def talk_word(bot, update):
        answer = config.talk_word_error_answer
        temp = ''
        try:
            temp = model.make_sentence_with_start(update.message.text)
        except KeyError:
            print('Could not create sentence with ' + update.message.text)
            bot.send_message(chat_id=update.message.chat_id, text=answer)
        finally:
            if temp is not None:
                answer = temp
            bot.send_message(chat_id=update.message.chat_id, text=answer)

    start_handler = CommandHandler(config['start_string'], start)
    talk_handler = CommandHandler(config['talk_string'], talk)
    talk_word_handler = MessageHandler(Filters.text, talk_word)
    dispatcher.add_handler(talk_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(talk_word_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()

