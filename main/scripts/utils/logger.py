import os
import logging
import sys
from inspect import getframeinfo, stack


DEBUG_ON = False


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def LOG_INFO(*text):
    textstr = ''.join(text)
    caller = getframeinfo(stack()[1][0])
    text = "[INFO] %s:%d: %s" % (caller.filename, caller.lineno, textstr)
    colored_text = colored(190, 190, 190, text)
    print(colored_text)


def LOG_DEBUG(*text):
    textstr = ''.join(text)
    caller = getframeinfo(stack()[1][0])
    text = "[DEBUG] %s:%d: %s" % (caller.filename, caller.lineno, textstr)
    colored_text = colored(100, 100, 105, text)
    if DEBUG_ON:
        print(colored_text)


def LOG_WARNING(*text):
    textstr = ''.join(text)
    caller = getframeinfo(stack()[1][0])
    text = "[WARNING] %s:%d: %s" % (caller.filename, caller.lineno, textstr)
    colored_text = colored(175, 175, 0, text)
    print(colored_text)


def LOG_ERROR(*text):
    textstr = ''.join(text)
    caller = getframeinfo(stack()[1][0])
    text = "[ERROR] %s:%d: %s" % (caller.filename, caller.lineno, textstr)
    colored_text = colored(255, 0, 0, text)
    print(colored_text)