import os

import logging
from telegram import Update
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = " ".join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


def main():
    token = open(os.path.join(__file__, "../.token")).readline().strip()
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    caps_handler = CommandHandler("caps", caps)
    application.add_handler(caps_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
