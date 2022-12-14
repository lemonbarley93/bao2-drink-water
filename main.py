import telegram
import time
import telebot
import schedule
from config import BOT_TOKEN, API_KEY,IDS_ALLOWED

bot = telegram.Bot(token='5756035785:AAG7pD29YEfZuAojWEfEIkaMt3c-WG_y64k')

def send_message():
	chat_ids = [322888294, 484011551] # list of chat IDs
	message = 'Sorry for the delayed function~ My master just corrupted my files! \U0001F97A\U0001F624 \n\n You know what time it is?! It\'sssssssssss time to grow your HAIRRRRR!!! Drink some water would you?! DRINK NOW!'

	for chat_id in chat_ids:
	    bot.send_message(chat_id=chat_id, text=message)

schedule.every(3600).seconds.do(send_message)

while True:
	schedule.run_pending()
	time.sleep(10)
