from loguru import logger

logger.add(
    "teamapp.log",
    format="{time}\t|\t{level}\t|\t{message}",
    level="INFO",
    rotation="10MB",
    compression="zip",
)
