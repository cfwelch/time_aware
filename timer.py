

import time, os

from playsound import playsound
from argparse import ArgumentParser

def remain(num_min):
    os.system("notify-send --urgency=critical -i ~/workspace/data/icons/hourglass.png '" + str(num_min) + " minutes remain...'")

def done():
    os.system("notify-send --urgency=critical -i ~/workspace/data/icons/hourglass3.png 'Time is up!'")

# Parse arguments
parser = ArgumentParser()
parser.add_argument("-m", "--minutes", dest="minutes", help="Number of minutes to wait for", default=30, type=int)
parser.add_argument("-aa", "--alert-at", dest="alert_at", help="Minute interval of alerts", default=5, type=int)
opt = parser.parse_args()

rem_time_min = opt.minutes
while rem_time_min > 0:
    remain(rem_time_min)
    sleep_interval = min(rem_time_min, opt.alert_at)
    time.sleep(sleep_interval*60)
    rem_time_min -= sleep_interval

playsound('ting.mp3')
done()
