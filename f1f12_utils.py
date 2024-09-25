
import logging
logger = logging.getLogger(__name__)

def initiateLogging():
    LOG_FORMAT = '[%(levelname)s] [%(filename)s(%(funcName)s:%(lineno)d) %(asctime)s] %(message)s'
    
    # logging.basicConfig(filename="f1f12log.log",level=logging.DEBUG)
    logging.basicConfig(filename="f1f12log.log", level=logging.DEBUG, format=LOG_FORMAT)
    logging.info("Started.")

def drawLine():
    logger.debug ("------------------------------------------------------------------------------------------")

def startProgram(progname = ""):
    initiateLogging()
    # drawLine()
    logger.debug ("Program started!")

def endProgram(progName = ""):
    logger.debug ("Program Ended!")
    # drawLine()
