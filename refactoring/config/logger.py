import logging
from logging import log
import logging.config

from refactoring.config.const import LogLevel

cnf = {
    'version': 1,
    # │ fileConfig의 disable_existing_loggers가 하위 호환성 때문에 활성화되어 있으니 주의하세요.
    # │ fileConfig()가 호출되기 전 루트가 아닌 로거들은 disable_existing_loggers 옵션을
    # ↓ 명시적으로 False로 바꾸기 전까지는 비활성화됩니다. dictConfig()를 사용하는 경우도 마찬가지입니다
    'disable_existing_loggers': False,
    'formatters': {
        'console_fmt': {
            '()': 'colorlog.ColoredFormatter',
            'format': f"%(log_color)s%(asctime)-15s [%(levelname)s] "
                      f"file:%(filename)s, line:%(lineno)d, %(message)s",
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'NOTICE': 'cyan,bg_bold_white',
                'ERROR': 'red',
                'USER': 'purple',
                'CRITICAL': 'bold_red,bg_black',
            },
        },
    },
    'handlers': {
        # 콘솔 출력용 핸들러
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'console_fmt'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler'
        }
    },
}


def init_logger():
    logging.config.dictConfig(cnf)
    logging.FileHandler
    '''
    CRITICAL = 50
    USER = 45
    ERROR = 40
    NOTICE = 35
    WARNING = 30
    INFO = 20
    DEBUG = 10
    '''
    logging.addLevelName(35, 'NOTICE')
    logging.addLevelName(45, 'USER')


def debug(msg):
    log(LogLevel.DEBUG, msg)


def info(msg):
    log(LogLevel.INFO, msg)


def warn(msg):
    log(LogLevel.WARNING, msg)
