# -*- coding: utf-8 -*-

import  config
import sys
import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            "%(asctime)s %(process)s %(levelname)s %(module)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt':
            "%Y-%m-%dT%H:%M:%S"
        },
        'simple': {
            'format':
            '%(levelname)s %(module)s [%(pathname)s:%(lineno)s] %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file-lib': {
            'level': 'DEBUG',
            'delay': True,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': 10,
            'when': 'D',
            'interval': 3,
            'filename': '/var/log/hyhive/hyhive-lib.log',
            'formatter': 'verbose'
        },
        'file-api': {
            'level': 'DEBUG',
            'delay': True,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'backupCount': 10,
            'when': 'D',
            'interval': 3,
            'filename': '/var/log/hyhive/hyhive-api.log',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file-api', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'log.lib': {
            'handlers': ['file-lib'],
            'level': 'INFO',
            'propagate': False
        }
    }
})


class Base():
    def __init__(self):
        pass


def init():
    #    sys.setdefaultencoding('utf8')
    init_config()


def init_config():
    ret = config.HyhiveConfig.load_config(config.CONFIG_DEF_FILE_NAME)
    if ret[0] == 0:
        for config_item in ret[1].keys():
            setattr(sys.modules[__name__], config_item,
                    ret[1].get(config_item))
    else:
        print "error"
    ret = config.HyhiveConfig.load_config(config.CONFIG_SET_FILE_NAME)
    if ret[0] == 0:
        for config_item in ret[1].keys():
            setattr(sys.modules[__name__], config_item,
                    ret[1].get(config_item))
    else:
        print "error"


init()

if __name__ == "__main__":
    print getattr(sys.modules[__name__], "SUCCESS")
    pass
