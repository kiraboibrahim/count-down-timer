import sys

import pyfiglet


def format_time(t):
    minutes = " ".join(list("{:02d}".format(t.minutes)))
    seconds = " ".join(list("{:02d}".format(t.seconds)))
    return pyfiglet.figlet_format("{} : {}".format(minutes, seconds))