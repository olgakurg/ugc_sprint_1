import logging
from logging import Formatter, Logger, StreamHandler

import orjson as json


class JsonFormatter(Formatter):
    """
    Formatter for logging records in JSON format.
    """

    def __init__(self) -> None:
        super(JsonFormatter, self).__init__()

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified record as JSON.

        Args:
            record (logging.LogRecord): The record to format.

        Returns:
            str: The formatted record.
        """
        json_record = {"message": record.getMessage()}
        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]
        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)
        return json.dumps(json_record).decode('utf-8')


logger: Logger = logging.root
handler: StreamHandler = StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.DEBUG)

logging.getLogger("uvicorn.access").disabled = True
