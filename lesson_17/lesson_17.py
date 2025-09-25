# logging, reporting, read of test data
from logg import logger
# import logging.config
#
# logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding="utf-8")
# logging.config.fileConfig("lesson_17\\log_config.ini", disable_existing_loggers=False)
#logger = logging.getLogger("sampleLogger")
def tratata():
    logger.debug('Це повідомлення рівня DEBUG')  # 10
    logger.info('Це повідомлення рівня INFO')  # 20

def lyalyalya():
    logger.warning('Це повідомлення рівня WARNING')  # 30
    logger.error('Це повідомлення рівня ERROR')  # 40
    logger.critical('Це повідомлення рівня CRITICAL')  # 50

if __name__ == "__main__":
    tratata()
    lyalyalya()
