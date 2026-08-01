from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, ALLOWED_USER_ID
from database import init_db, save
from ollama_client import ask


async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ALLOWED_USER_ID:
        return

    if not update.message or not update.message.text:
        return

    user_text = update.message.text

    await update.message.chat.send_action("typing")

    save(ALLOWED_USER_ID, "user", user_text)

    answer = ask(user_text)

    save(ALLOWED_USER_ID, "assistant", answer)

    await update.message.reply_text(answer)


def main():

    print("=" * 50)
    print("Telegram Bot Started")
    print("Model : gemma3:1b")
    print("Ollama Connected")
    print("=" * 50)

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            msg,
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()