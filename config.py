import os

API_ID = API_ID = 28404611

API_HASH = os.environ.get("API_HASH", "6d00594e457389e571d8dfc9e714fecf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7470181327:AAH4FhiBzPAxAGwerwFLk1ioWGnjTFwx_o8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6341175473))

LOG = -1002101234349

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6341175473 6959409818").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


