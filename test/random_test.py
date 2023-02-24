import logging, random

logger = None

def init_logger():
    global logger
    logger = logging.getLogger("random-text")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("random.log")
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s [%(name)s] - %(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

def random_text():
    # print(logger)
    for i in range(100):
        if i % 12 == 0:
            logger.info("Epoch - nums: {}, count: {}.".format(
                i // 12,
                random.randint(2000, 3000)))
        
        logger.info("Batch - year: {}, value: {}.".format(
            random.randint(0, 100),
            random.randint(2000, 3000)))


if __name__ == '__main__':
    init_logger()
    if logger != None:
        random_text()
