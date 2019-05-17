import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# import os
# defaultLevel = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))
# logger.setLevel(defaultLevel)
logger.setLevel(logging.INFO)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.warning(type(logging.WARNING))
logger.error('This is an error')
logger.info('This is an info')
logger.debug('This is a debug')
