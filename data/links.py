import os


class Links:
    HOST = f'https://{os.environ['STAGE']}.demo.ultimeta.ru'
    # $env:STAGE="brusnika-qa"; pytest -sv
    # $env:STAGE="brusnika"; pytest -sv

    FRAME_LINK = f'{HOST}/frame/index.html'
    PROFILE_LINK = f'{HOST}/users/profile'




