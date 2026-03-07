import os
import sys


def get_platform():
    return sys.platform


def clear():
    platform = get_platform()
    if platform.lower() == "win32":
        os.system("cls")
    else:
        os.system("clear")
