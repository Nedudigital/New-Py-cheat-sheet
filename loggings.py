import logging
import traceback
'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

create your own logger in your module
logger = logging.getLogger(__name__)
logger.info('hello from helper')
logger.propagate = False
if you don't want this to reflect in the other module
it's good practice to create your own logger

log handlers are used to dispatch messages to the appropriate stream
'''
logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

'''this generated a file.org folder'''
'''for logging you will have to go through the docs if you need to use it, say for troubleshooting and stuff'''
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True) 

'''if you dont know the error you can use a traceback '''       
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error('This error is %s', traceback.format_exc()) 
