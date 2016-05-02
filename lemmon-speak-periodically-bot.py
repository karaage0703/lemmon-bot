# -*- coding: utf-8 -*-
# import twython
import sys
import subprocess
import random
from time import sleep

probability = 0.2       # probability of bot working
bot_period = 1.0       # bot working period

def speak():
    if random.random() < probability:
        cmd = "./lemmon-speak-bot.sh" 
        subprocess.call(cmd, shell=True)
        print("hello")

    else:
        print("silent")



if __name__ == '__main__':
    while 1:
        sleep(bot_period)
        print("bot working")
        speak()
