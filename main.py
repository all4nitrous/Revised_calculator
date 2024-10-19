import os
import logging


# My setup (revise)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    
    environment = os.getenv('ENVIRONMENT', 'production')
    logger.info(f"Running in {environment} mode")

    
    logger.info("Application started successfully")

if __name__ == "__main__":
    main()
