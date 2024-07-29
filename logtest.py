import logging

logging.basicConfig(level=logging.NOTSET)

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

logger.error('error...')
logger.warning('warning...')
logger.info('info...')
logger.debug('debug...')