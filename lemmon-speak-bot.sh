#!/bin/bash

cd `dirname $0`
cd TextGenerator
python GenerateText.py 2 > ../speak.txt
cd ..
~/aquestalkpi/AquesTalkPi -f speak.txt | aplay
