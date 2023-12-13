import auth_data
import openai
import translators.server as tss
from run_vk import uploader
import requests


def download_image(url):
    p = requests.get(url)
    out = open("avatar.jpg", "wb")
    out.write(p.content)
    out.close()


def make_pic(answer):
    prompt = tss.google(answer, 'ru', 'en') + 'painting'
    openai.api_key = auth_data.openai_key
    image = openai.Image.create(
        prompt=prompt,
        n=1,
        size='256x256'
    )
    url = image['data'][0]['url']
    download_image(url)
    img = uploader.photo_messages('avatar.jpg')

    return img

