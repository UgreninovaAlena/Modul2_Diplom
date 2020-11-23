from urllib.parse import urlencode

from ChatBot import BOT

if __name__ == '__main__':

    URL_for_autorize = 'https://oauth.vk.com/authorize'
    ID = 7656145
    param = {
        'client_id': ID,
        'display': 'popup',
        'scope': 'photos, status',
        'response_type': 'token',
        'v': 5.89}
    url = '?'.join((URL_for_autorize, urlencode(param)))
    print(url)

a = BOT()
a.chat()
