# Bot Name - dottingdot
# Bot Username - dottingdot_bot

# Bot link - t.me/dottingdot_bot
# You can use this link to get to my(i.e., this bot) bot


from telegram import Update
import telegram.ext as tg


async def start(update: Update, context: tg.ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text("Hello!! I am ready to go.. The question is... Are you.... I like using a lot of dots.....")
  await update.message.reply_text("Type '/help' to.. get the list of commands....")

async def help(update: Update, context: tg.ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text("Here.. I am to help...")

async def hello(update: Update, context: tg.ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(f'Hi There... {update.effective_user.first_name}... I am dottingdot bot. I can\'t help you in any way!! As I know nothing..')

tokenFile = open("token.txt","r")
Token = tokenFile.read()
tokenFile.close()
app = tg.ApplicationBuilder().token(Token).build()


app.add_handler(tg.CommandHandler("start", start))
app.add_handler(tg.CommandHandler("help", help))
app.add_handler(tg.CommandHandler("hello", hello))


app.run_polling()
