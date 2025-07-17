API_PREFIX = {
    'authentication': {
        'sign_in': '/authentication/sign-in',
        'verify_session': '/authentication/verify/session?Authorization={access_token}'
    }
}

API_VERSION = 'v1'
API_URL = f'http://192.168.1.92:7500/api/{API_VERSION}'