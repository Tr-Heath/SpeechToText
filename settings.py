# https://github.com/miguelgrinberg/microblog/blob/master/config.py
# https://pypi.org/project/python-dotenv/

import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_TEST = os.environ.get('SECRET_TEST')
    something='something'