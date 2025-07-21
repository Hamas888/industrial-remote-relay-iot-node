# main.py

import  logging
from    utils.logger                import getLogger
from    services.device_manager     import DeviceManager

logger = getLogger("Main")
logging.getLogger("aioice.ice").setLevel(logging.WARNING)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting device manager...")
    try:
        device = DeviceManager()
        device.run()
    except Exception as e:
        device.close()
        logger.error(f"Unexpected error: {e}")