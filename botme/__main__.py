import importlib

from botme import updater, logger, j, OWNER
from botme.core import modules, function, database
from botme.core.database import db

j = j.scheduler

for module in modules:
    importlib.import_module(f"botme.core.{module}")


def main():
    updater.bot.send_message(chat_id=OWNER, text="Restarting...")
    j.start()
    updater.start_polling()
    logger.info("Listening using polling")

    updater.idle()


if __name__ == "__main__":
    main()
