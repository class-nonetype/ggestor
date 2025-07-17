from os import getenv
from dotenv import load_dotenv
load_dotenv()


API_PREFIX = {
    'authentication': {
        'sign_in': '/authentication/sign-in',
        'verify_session': '/authentication/verify/session?Authorization={access_token}'
    }
}

API_VERSION = 'v1'
API_URL = getenv('API_URL') + API_VERSION

DATABASE_URL = getenv('DATABASE_URL')