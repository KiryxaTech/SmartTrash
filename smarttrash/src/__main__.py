# KiryxaTech (c) 2025. The MIT License.

import logging
from datetime import datetime
from pathlib import Path


def setup_logger() -> logging.Logger:
    """Creates and configures the logger with file output based on current date and time."""
    log_dir = Path("smarttrash/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")

    logger = logging.getLogger("smarttrash")
    logger.setLevel(logging.DEBUG)

    # Console handler (optional)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # Log format
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def main(logger: logging.Logger):
    logger.debug("Main function started.")
    # Your main logic goes here...
    logger.debug("Main function finished.")


if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Smart Trash has started.")
    try:
        main(logger)
        logger.info("Smart Trash has stopped. Code 0.")
    except Exception as e:
        logger.exception("An error occurred during execution.")