import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID", "1747534"))
API_HASH = environ.get("API_HASH", "5a2684512006853f2e48aca9652d83ea")
SESSION = environ.get("SESSION", "1BVtsOIoBu7EpfDM-A0CLUUGBDbsQZaOwV8KgeH3boTAQm1Gbgfa_awtTarfSeuiEkOUQwC-meI_mEaXp348ecai6vygMsQHHpDyZzHW8HTeD1VVG9Hqms2PE65BGWx--Waj91JurHua9X0ghHYfovaE_tZNvnGj98mYpqKri8l8eA_Rm00yKMRC1rQMwWB0Ive8Z_f39FcIF2TTeIAiB4Fmqpt6RqpBau7j0R66ndu0wy3Nsdurvfduf8qKgfkDtCFdW83pwns4VJUt_zeHWf2N9mNtJYPu4uXt5_cgKRgzF9zffWPc0YymoOKBh8B-cA9aFb84cXbGviS7kMbKzEPoDp1lmIsE=")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001696873364"))


if SESSION is not None:
    session = StringSession(str(SESSION))
else:
    session = "pyrobot"

try:
    client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )
    client.start()
    
except Exception as e:
    print(e)

