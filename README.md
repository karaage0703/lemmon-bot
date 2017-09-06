# lemmon-bot
lemmon-chan bot

# Hardware
- Raspberry Pi 2 or 3
- Active speaker (optional)


# Setup
## Install packages
Execute following commands:
```sh
$ sudo apt-get update
$ sudo apt-get install mecab
$ sudo apt-get install libmecab-dev
$ sudo apt-get install mecab-ipadic-utf8
$ sudo apt-get install python-mecab
$ sudo pip install twython
```

## Install Aquestalk Pi
Download Aquestalk Pi from following site:  
[AquesTalk Pi](http://www.a-quest.com/products/aquestalkpi.html)

Move `aquestalkpi-20130827.tgz` to home directory(`/home/pi`) of raspberry pi, then execute following commands:

```sh
$ cd
$ tar xvzf aquestalkpi-20130827.tgz
$ cd aquestalkpi
```

## Test Aquestalk Pi
Connect active speaker to raspberry pi, then execute following command:
```sh
$ ./AquesTalkPi "hello" |  aplay
```
If setting is correct, you will hear that bot speaks "hello".

## Git clone and Generate DB file
Execute following commands:
```sh
$ git clone https://github.com/karaage0703/lemmon-bot.git
$ cd lemmon-bot
$ git clone https://github.com/karaage0703/TextGenerator.git
$ cd TextGenerator
$ python PrepareChain.py sample.txt
```

# Tweet from bot
Execute following command:
```sh
$ ./lemmon-tweet-bot.sh
```


# Bot speaking
Execute following command:
```sh
$ ./lemmon-speak-bot.sh
```

# Bot speaking periodically
Execute following command:
```sh
$ python lemmon-speak-periodically-bot.py
```


# License
This software is released under the MIT License, see LICENSE.

