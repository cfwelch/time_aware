

import psutil, time, os

from playsound import playsound
from argparse import ArgumentParser

#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = "~/workspace/data/icons"

icon1_loc = dir_path + "/hourglass.png"
icon2_loc = dir_path + "/hourglass3.png"

def remain(num_min):
    if psutil.OSX:
        os.system("osascript -e 'display notification \"" + str(num_min) + " minutes remain...\" with title \"{}\"'")
    elif psutil.LINUX:
        os.system("notify-send --urgency=critical -i " + icon1_loc + " '" + str(num_min) + " minutes remain...'")
    elif psutil.WINDOWS:
        print("Windows is not supported...")

def done():
    if psutil.OSX:
        os.system("osascript -e 'display notification \"Time is up!\" with title \"{}\"'")
    elif psutil.LINUX:
        os.system("notify-send --urgency=critical -i " + icon2_loc + " 'Time is up!'")
    elif psutil.WINDOWS:
        print("Windows is not supported...")

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
