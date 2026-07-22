import os
import edge_tts
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8860740600:AAFsoJ0MOxu4fBRC8vZHTQ9y9lWH_zY1Wog"

VOICE = "fa-IR-DilaraNeural"

async def text_to_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    output = "output.mp3"

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output)

    await update.message.reply_voice(voice=open(output, "rb"))

    os.remove(output)

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_voice))

print("Bot is running...")

app.run_polling()