# -*- coding: utf-8 -*-
import sys
import subprocess
import random
from time import sleep

probability = 0.2       # probability of bot working
bot_period = 1800.0       # bot working period

def tweet():
    if random.random() < probability:
        cmd = "./lemmon-tweet-bot.sh"
        subprocess.call(cmd, shell=True)
        print("tweet")

    else:
        print("silent")



if __name__ == '__main__':
    while 1:
        tweet()
        print("bot working")
        sleep(bot_period)
