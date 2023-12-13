from run_vk import vk
import make_keyboards
import random
from make_pic import make_pic
from get_key_words import get_key_words
import datetime


def main():
    while True:
        print(datetime.datetime.now())
        messages = vk.method('messages.getConversations', {'offset': 0, 'count': 1, 'filter': 'unanswered'})
        if messages['count'] != 0:
            text = messages['items'][0]['last_message']['text']
            user_id = messages['items'][0]['last_message']['from_id']
            try:
                print(messages['items'][0]['last_message']['payload'])
            except:
                pass
            if text.lower() == 'начать':
                vk.method('messages.send', {'user_id': user_id, 'message': 'Бот научился делать аватары!'
                                                                           ' Пожалуйста, не делайте больше '
                                                                           'одного автара, на это расходуется пробный '
                                                                           'период очень недешевого сервиса!',
                                            'random_id': random.randint(1, 1000),
                                            'keyboard': make_keyboards.base_keyboard.get_keyboard()})
            elif text.lower() == 'получить персональный аватар':
                vk.method('messages.send', {'user_id': user_id,
                                            'message': 'Пожалуйста, подождите, задача не из простых...',
                                            'random_id': random.randint(1, 1000)})
                img = make_pic(get_key_words(user_id))
                media_id = str(img[0]['id'])
                owner_id = str(img[0]['owner_id'])
                vk.method('messages.send', {'user_id': user_id,
                                            'message': 'Аватар готов!',
                                            'random_id': random.randint(1, 1000),
                                            'attachment': 'photo' + owner_id + '_' + media_id,
                                            'keyboard': make_keyboards.avatar_keyboard.get_keyboard()})

            elif text.lower() == 'попробовать снова!':
                vk.method('messages.send', {'user_id': user_id,
                                            'message': 'На данный момент такая функция недоступна, '
                                                       'но все изменится. Скоро.',
                                            'random_id': random.randint(1, 1000),
                                            'keyboard': make_keyboards.avatar_keyboard.get_keyboard()})

            elif text.lower() == 'мне нравится':
                vk.method('messages.send', {'user_id': user_id,
                                            'message': 'Ура! А скоро улучшится и качество фотографий',
                                            'random_id': random.randint(1, 1000),
                                            'keyboard': make_keyboards.answer_keyboard.get_keyboard()})

            elif text.lower() == 'мне не нравится':
                vk.method('messages.send', {'user_id': user_id,
                                            'message': 'Эх... Работы по улучшению бота активно ведутся, '
                                                       'надеюсь, что скоро он сможет вас порадовать.',
                                            'random_id': random.randint(1, 1000),
                                            'keyboard': make_keyboards.answer_keyboard.get_keyboard()})


if __name__ == '__main__':
    main()
