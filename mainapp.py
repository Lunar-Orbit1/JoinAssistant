# Claym1x, 2024
# This is a program that simplifies editing your ROBLOX join settings for events

from requests import post as postreq
from requests import get as getreq
from time import sleep as sl
import platform
import os, logger

version = "V0.3" #Current software version

def isConfiguredProperly():
    if os.path.exists(".env"):
        return True
    else:
        return False

def controlOrCommand():
    """Returns control if the user is on windows, or command if the user is on MacOS"""
    if platform.system() == "Darwin":
        return "command"
    else:
        return "control"
    
def askYN(question:str):
    """Asks a yes or no question. Will recurse if something other than yes/no is provided"""
    try:
        input1 = input(question+ " (yes/no) \n> ").lower()
        if input1 != "n" and input1 != "no" and input1 != "yes" and input1 != "y":#Pretty jenky, not the best code. TODO: Rewrite
            # The answer isn't valid, recurse and return the recursion
            return askYN(question)
        else:
            #Input IS valid, check for y/n
            if input1 == "n" or input1 == "no":
                return False
            else:
                return True
    except KeyboardInterrupt:
        logger.FAIL("Shutting down..")
        sl(1)
        exit(0)


def startCLI():
    """The main input function. This starts the command line basically"""
    try:
        input1 = input("> ")
    except KeyboardInterrupt:
        logger.FAIL("Shutting down..")
        sl(1)
        exit(0)

if isConfiguredProperly() == False:
    logger.FAIL("Join Assistant is not configured properly.")
    logger.FAIL("Read README.md for information on how to start and configure this program")

print(f"Join Assistant Version {version}")
logger.WARN(f"Close this terminal or press {controlOrCommand()}+C to exit")
askYN("hi")