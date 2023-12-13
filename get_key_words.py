import requests
from auth_data import app_access_token as token


def get_key_words(user_id):
    user_url = f'https://api.vk.com/method/users.getSubscriptions?user_id={user_id}&extended=1&count=20&fields=activity,description&access_token={token}&v=5.131'
    req = requests.get(user_url)
    src = req.json()
    answer = ''
    try:
        for item in src['response']['items']:
            string = item['activity']
            print(item['name'])
            answer += string + ' '
    except KeyError:
        pass

    return answer

