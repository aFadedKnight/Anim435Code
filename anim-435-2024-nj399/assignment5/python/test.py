import os, logging, json

logger = logging.getLogger(__name__)

FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s"

logging.basicConfig(filename='F:/School/TechDirecting/Week4/Project/log.txt',level=logging.INFO, format=FORMAT)
logger.info('Starting')