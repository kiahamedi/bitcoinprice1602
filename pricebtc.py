#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd = "./btc.sh"

lcd.begin(16, 1)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    lcd.clear()
    price = run_cmd(cmd)
    lcd.begin(16,2)
    lcd.setCursor(5,0)
    lcd.message("Bitcoin")
    lcd.setCursor(0,1)
    lcd.message('Price: %s' % (price))
    sleep(60)
