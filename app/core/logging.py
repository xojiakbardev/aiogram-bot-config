import os
import logging
from logging.config import dictConfig

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
        },
        "json": {
            "format": '{"time": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s"}'
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "file_rotating": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{LOG_DIR}/app.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "default",
            "level": "INFO",
            "encoding": "utf-8"
        },
        "json_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{LOG_DIR}/app.json.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 3,
            "formatter": "json",
            "level": "INFO",
            "encoding": "utf-8"
        }
    },

    "root": {
        "handlers": ["console", "file_rotating", "json_file"],
        "level": "DEBUG",
    },
}


def setup_logging():
    dictConfig(LOGGING_CONFIG)


def get_logger(name: str = ""):
    return logging.getLogger(name)
