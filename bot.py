from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import app
updater = Updater(token='BOT_API')
dispatcher = updater.dispatcher
def textMessage(bot, update):
    bot.send_message(chat_id)
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(callback_handler)

updater.start_polling(clean=True)
