import sys
from loguru import logger as process_logger


process_logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="my_module", level="INFO"
    )

process_logger.add("load_data.log", rotation="100 MB")
