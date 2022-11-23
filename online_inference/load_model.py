import logging
import os

import yadisk
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()


def main() -> None:
    logging.info("Getting disk info...")

    DISK_TOKEN = os.environ.get("DISK_TOKEN")
    MODEL_URL = os.environ.get("MODEL_URL")
    MODEL_SAVE_PATH = os.environ.get("MODEL_PATH")

    logging.info("Accessing disk...")

    disk = yadisk.YaDisk(token=DISK_TOKEN)

    logging.info("Downloading model...")

    disk.download(MODEL_URL, MODEL_SAVE_PATH)

    logging.info("Done.")


if __name__ == "__main__":
    main()
