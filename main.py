from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from OSINT import *

async def main():
    await clear_bot_webhooks()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("number", number_lookup))
    app.add_handler(CommandHandler("vehicle", vehicle_lookup))
    app.add_handler(CommandHandler("ip", ip_lookup))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("🚀 Bot is running...")
    await app.run_polling()

import asyncio
asyncio.run(main())
