import logging.config

from logger import logging_config
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")


if __name__ == '__main__':
    main()
