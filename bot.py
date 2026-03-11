import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from handlers.chat import chat_with_ai
from handlers.image import generate_image
from handlers.video import generate_video
from handlers.music import generate_music

load_dotenv()
TOKEN = os.getenv("8045986755:AAF9df3RHzDFCvg5nMw-0cJiVPXQdkoqNso")
reply_keyboard = [["💬 Чат с ИИ", "🖼 Генерация фото"], ["🎥 Генерация видео", "🎵 Создание музыки"]]

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я Синтияя — миниап ИИ бот. Выберите функцию:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "💬 Чат с ИИ":
        update.message.reply_text("Введите вопрос:")
        context.user_data['mode'] = 'chat'
    elif text == "🖼 Генерация фото":
        update.message.reply_text("Опишите желаемое изображение:")
        context.user_data['mode'] = 'image'
    elif text == "🎥 Генерация видео":
        update.message.reply_text("Опишите видео:")
        context.user_data['mode'] = 'video'
    elif text == "🎵 Создание музыки":
        update.message.reply_text("Опишите музыку:")
        context.user_data['mode'] = 'music'
    else:
        mode = context.user_data.get('mode')
        if mode == 'chat':
            reply = chat_with_ai(text)
            update.message.reply_text(reply)
        elif mode == 'image':
            img = generate_image(text)
            update.message.reply_photo(img)
        elif mode == 'video':
            video_url = generate_video(text)
            update.message.reply_text(f"Сгенерированное видео: {video_url}")
        elif mode == 'music':
            music = generate_music(text)
            update.message.reply_audio(music)
        else:
            update.message.reply_text("Выберите функцию из меню!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
