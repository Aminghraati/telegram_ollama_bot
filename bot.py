
from telegram import Update
from telegram.ext import Application,MessageHandler,filters,ContextTypes
from config import BOT_TOKEN,ALLOWED_USER_ID
from database import init_db,save
from ollama_client import ask

async def msg(update:Update,ctx:ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id!=ALLOWED_USER_ID:return
    t=update.message.text
    save(ALLOWED_USER_ID,"user",t)
    ans=ask(t)
    save(ALLOWED_USER_ID,"assistant",ans)
    await update.message.reply_text(ans)

init_db()
app=Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,msg))
app.run_polling()
