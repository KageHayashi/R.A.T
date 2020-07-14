import os
import random
from colors import color
from pyfiglet import Figlet

def clear_screen():
    os.system('clear')

yes = ["yes", "y", "yah", "mhm", "yessir", "yeah", "yea", "Y"]
def yesno():
    return (input("Continue y/n: ") in yes)


color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
random.shuffle(color_random)

ratlogo = color_random[0] + Figlet(font='slant').renderText('R . A . T')
weatherlogo = color_random[0] + Figlet(font='slant').renderText('Weather')
description = color.NOTICE + "--------Random Accessible Tools--------"
ratprompt = "rat~# "
weatherprompt = "weather~# "