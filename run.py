"""
Main function to run game the file for 'Word-It'
"""

import sys
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# install & import pyfiglet module from https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
import pyfiglet

result = pyfiglet.figlet_format("Word-It", font = "digital")
print(result)
