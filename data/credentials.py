import os
from dotenv import load_dotenv

load_dotenv()


class Credentials():
    if os.environ["STAGE"] == "brusnika-qa":
        LOGIN_ORGANIZER = os.getenv("LOGIN_ORGANIZER_QA")
        LOGIN_PARTICIPANT_ONE = os.getenv("LOGIN_PARTICIPANT_ONE_QA")
        LOGIN_PARTICIPANT_TWO = os.getenv("LOGIN_PARTICIPANT_TWO_QA")
        PASSWORD = os.getenv("PASSWORD_QA")
    elif os.environ["STAGE"] == "brusnika":
        LOGIN = os.getenv("LOGIN_DEMO")
        PASSWORD = os.getenv("PASSWORD_DEMO")
