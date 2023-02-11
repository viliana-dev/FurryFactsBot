from classify import classify
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import numpy as np
import cv2


def image_handler(update, context):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        image = context.bot.get_file(file_id)
        image_data = image.download_as_bytearray()
        numpy_array = np.frombuffer(image_data, dtype=np.uint8)
        image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
        result = classify(image)
        update.message.reply_text(result)

def main():
    updater = Updater(os.environ.get('TELEGRAM_BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
