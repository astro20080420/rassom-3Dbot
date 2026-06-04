import telebot
import fal_client
import os

# Tokenni kod ichiga emas, server muhitidan (Variables) o'qiymiz
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 3D model uchun ta'rif yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        msg = bot.send_message(message.chat.id, "3D model yaratilmoqda, biroz kuting...")
        handler = fal_client.submit(
            "fal-ai/tripo-sr",
            arguments={"prompt": message.text},
        )
        result = handler.get()
        model_url = result["mesh_url"]
        bot.edit_message_text(f"Tayyor! Modelingizni yuklab oling: {model_url}", chat_id=message.chat.id, message_id=msg.message_id)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

# Botni ishga tushirish
if __name__ == "__main__":
    bot.infinity_polling()