from instabot import Bot

bot = Bot()
bot.login(username="devd.iwan", password="ayhanayhan@#1")

# دریافت پیام‌های جدید
messages = bot.get_unread_messages()

for message in messages:
    user_id = message['user_id']
    text = message['text']
    
    # پاسخ ساده
    if "سلام" in text:
        bot.send_message("سلام! چطور می‌تونم کمکت کنم؟", user_id)
    else:
        bot.send_message("پیامت رو دریافت کردم، بزودی جواب میدم.", user_id)
