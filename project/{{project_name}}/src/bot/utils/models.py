from enum import Enum


class Commands:
    START = "start"
    HELP = "help"


class Actions(str, Enum):
    ACTION = "action"
    CANCEL = "cancel"
