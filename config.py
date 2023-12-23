from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    CID: str = os.getenv('CID')

    P_URL: str = os.getenv('P_URL')
    P_USER: str = os.getenv('P_USER')
    P_PASS: str = os.getenv('P_PASS')

    SLEEP_TIME: int = int(os.getenv('SLEEP_TIME'))

config = Config()