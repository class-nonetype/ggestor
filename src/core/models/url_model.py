from src.core.utils import API_URL, API_PREFIX

class URLModel:


    @staticmethod
    def get_url(key: str) -> str:
        url = {
            'sign_in': API_URL + API_PREFIX['authentication']['sign_in'],
            'verify_session': API_URL + API_PREFIX['authentication']['verify_session']
        }
        return url[key]
