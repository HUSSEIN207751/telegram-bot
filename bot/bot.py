from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import pyotp

BOT_TOKEN = "8203248734:AAGhqlUVt8-lU0hpSq52S3xLgDAL1vIG7rQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 ابعت مفتاح 2FA الخاص بك."
    )

async def generate_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    secret = update.message.text.strip().replace(" ", "")

    try:
        totp = pyotp.TOTP(secret)
        code = totp.now()

        await update.message.reply_text(
            f"✅ كود المصادقة الحالي:\n\n`{code}`",
            parse_mode="Markdown"
        )

    except:
        await update.message.reply_text(
            "❌ المفتاح غير صحيح."
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, generate_code)
)

print("✅ Bot Running...")
app.run_polling()