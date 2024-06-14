import os

API_ID = API_ID = 28404611

API_HASH = os.environ.get("API_HASH", "6d00594e457389e571d8dfc9e714fecf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7282524458:AAEkpEZX0T8iqcxRtRXAHeHk4WIOZ1IQZvs")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6959409818))

LOG = -1002242340368

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6436809802 6959409818").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


