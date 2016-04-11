#!/bin/bash

cd `dirname $0`
cd TextGenerator
python GenerateText.py 2 > ../tweet.txt
cd ..
python lemmon-tweet-bot.py tweet.txt
