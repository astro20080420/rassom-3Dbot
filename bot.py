import telebot
import fal_client
import os

TOKEN = "8744906457:AAHFvUOS4Fnfv8GmZAsCGXTwe9gp-BeQmpg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 3D model uchun ta'rif yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_message(message.chat.id, "3D model yaratilmoqda, kuting...")
        handler = fal_client.submit("fal-ai/tripo-sr", arguments={"prompt": message.text})
        result = handler.get()
        bot.send_message(message.chat.id, f"Tayyor: {result['mesh_url']}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Xatolik: {str(e)}")

bot.infinity_polling() oling: {model_url}", chat_id=message.chat.id, message_id=msg.message_id)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

# Botni ishga tushirish
if __name__ == "__main__":
    bot.infinity_polling()