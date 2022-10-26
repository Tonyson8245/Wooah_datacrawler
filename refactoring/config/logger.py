import logging
from logging import log

from refactoring.config.const import LogLevel

# todo 임시로 로그 레벨 warn에서 debug으로 내림. 나중에 로그 config 만들어서 설정할 때 없애주거나 수정할 것
logging.getLogger().setLevel(LogLevel.DEBUG)


def debug(msg):
    log(LogLevel.DEBUG, msg)


def info(msg):
    log(LogLevel.INFO, msg)


def warn(msg):
    log(LogLevel.WARNING, msg)
