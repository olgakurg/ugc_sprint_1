import json
import logging
import os
from logging import Formatter, Logger
from logging.handlers import RotatingFileHandler

from core.config import settings


class JsonFormatter(Formatter):
    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record):
        json_record = {}
        json_record["message"] = record.getMessage()
        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]
        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)

        return json.dumps(json_record)


if not os.path.exists(settings.log_dir):
    os.makedirs(settings.log_dir)
log_path = os.path.join(settings.log_dir, settings.log_file)

logger: Logger = logging.root
handler = RotatingFileHandler(filename=log_path, maxBytes=settings.log_size, backupCount=settings.log_backup_num)
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.DEBUG)

logging.getLogger("uvicorn.access").disabled = True
