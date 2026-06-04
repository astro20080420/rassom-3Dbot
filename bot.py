import telebot
import fal_client

bot = telebot.TeleBot("8744906457:AAHFvUOS4Fnfv8GmZAsCGXTwe9gp-BeQmpg")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 3D model uchun ta'rif yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Kuting, 3D model yaratilyapti...")
    try:
        handler = fal_client.submit("fal-ai/tripo-sr", arguments={"prompt": message.text})
        result = handler.get()
        bot.reply_to(message, f"Tayyor: {result['mesh_url']}")
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

bot.infinity_polling()
