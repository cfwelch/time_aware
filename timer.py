

import random, time, os

from pydub import AudioSegment
from pydub.playback import play
from argparse import ArgumentParser

timeup = AudioSegment.from_mp3("ting.mp3")

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = "."

icon1_loc = dir_path + "/hourglass.png"
icon2_loc = dir_path + "/hourglass3.png"
EXPIRE = 5*1000
LINUX_URGENCY = "" #--urgency=critical

def remain(num_min):
    hours = int(num_min/60)
    mins = num_min%60
    alert_str = str(mins) + " minutes remain..."
    if hours > 0:
        alert_str = str(hours) + " hours and " + alert_str
    os.system("notify-send " + LINUX_URGENCY + " -i " + icon1_loc + " '" + alert_str + "' -t " + str(EXPIRE))

def start():
    os.system("notify-send " + LINUX_URGENCY + " -i " + icon1_loc + " 'Starting!' -t " + str(EXPIRE))

def done():
    os.system("notify-send " + LINUX_URGENCY + " -i " + icon2_loc + " 'Time is up!' -t " + str(EXPIRE))

# Parse arguments
parser = ArgumentParser()
parser.add_argument("-m", "--minutes", dest="minutes", help="Number of minutes to wait for", default=30, type=int)
parser.add_argument("-aa", "--alert-at", dest="alert_at", help="Minute interval of alerts", default=5, type=int)
parser.add_argument("-r", "--random", dest="random", help="Randomly vary the amount of time between alarms", action="store_true", default=False)
parser.add_argument("-ra", "--range", dest="rrange", help="Sets the range of random to minutes +- this value", default=3, type=int)
parser.add_argument("-l", "--loop", dest="loop", help="Set a new timer when this one expires", default=False, action="store_true")
opt = parser.parse_args()

while(True):
    rem_time_min = opt.minutes
    if opt.random:
        rem_time_min = rem_time_min - opt.rrange + random.random() * 2 * opt.rrange

    while rem_time_min > 0:
        if not opt.random:
            remain(rem_time_min)
        else:
            remain(rem_time_min)
            # start()
        sleep_interval = min(rem_time_min, opt.alert_at)
        time.sleep(sleep_interval*60)
        rem_time_min -= sleep_interval

    play(timeup)
    done()

    if not opt.loop:
        break
