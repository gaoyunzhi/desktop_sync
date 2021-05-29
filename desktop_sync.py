#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram_util import log_on_fail
import album_sender
import threading
import plain_db
from telegram.ext import Updater
import os

with open('token') as f:
	token = f.read().strip()
tele = Updater(token, use_context=True)  # @weibo_subscription_bot
debug_group = tele.bot.get_chat(420074357)

existing = plain_db.loadKeyOnlyDB('existing')

@log_on_fail(debug_group)
def loopImp():
	for file in os.listdir('~/Desktop'):
		print(file)
		if existing.contain(file):
			continue
		if file.endswith('.jpg'):
			debug_group.send_photo(file)
		
def loop():
	loopImp()
	threading.Timer(10, loop).start() 

if __name__ == '__main__':
	threading.Timer(1, loop).start() 
	tele.start_polling()
	tele.idle()