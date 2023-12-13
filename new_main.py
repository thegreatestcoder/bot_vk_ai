from run_vk import vk
import requests
import new_keyboards
import random
from run_vk import uploader
from make_pic import make_pic
from get_key_words import get_key_words


def check_new(user_id):
    return True


def main():
    img = uploader.photo_messages('avatar.jpg')
    media_id = str(img[0]['id'])
    owner_id = str(img[0]['owner_id'])
    while True:
        messages = vk.method('messages.getConversations', {'offset': 0, 'count': 1, 'filter': 'unanswered'})
        print(messages)
        if messages['count'] != 0:
            message = messages['items'][0]
            user_id = str(message['last_message']['from_id'])
            try:
                payload = message['last_message']['payload']
                if payload == '{"command":"start"}':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Добро пожаловать',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.first_keyboard.get_keyboard()})
                elif payload == '0':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'То се хуе мое',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.first_keyboard.get_keyboard()})
                elif payload == '1':
                    if check_new(user_id):
                        vk.method('messages.send', {'user_id': user_id, 'message': 'Cоздаем ваш первый аватар',
                                                    'random_id': random.randint(1, 1000)})
                        img = make_pic(get_key_words(user_id))
                        media_id = str(img[0]['id'])
                        owner_id = str(img[0]['owner_id'])
                        vk.method('messages.send', {'user_id': user_id,
                                                    'message': 'Аватар готов!',
                                                    'random_id': random.randint(1, 1000),
                                                    'attachment': 'photo' + owner_id + '_' + media_id,
                                                    'keyboard': new_keyboards.main_keyboard.get_keyboard()})
                    else:
                        pass
                elif payload == '2':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Типо получил',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.main_keyboard.get_keyboard(),
                                                'attachment': 'photo' + owner_id + '_' + media_id})
                elif payload == '3':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'К сожалению, мы вынуждены'
                                                                               'сделать генерацию автаров платной ради'
                                                                               ' поддержания работы сервиса. Стоимсоть '
                                                                               'нового аватара - 10 рублей',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.payment_keyboard.get_keyboard()})
                elif payload == '5':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Генерация...',
                                                'random_id': random.randint(1, 1000)})
                    vk.method('messages.send', {'user_id': user_id,
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.make_mark_keyboard(user_id),
                                                'attachment': 'photo' + owner_id + '_' + media_id})

                elif payload == '4':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Типо анкета',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.make_mark_keyboard(user_id),
                                                'attachment': 'photo' + owner_id + '_' + media_id})
                elif payload == '6':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Ваше право',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.main_keyboard.get_keyboard()})

                elif payload[0] == '7':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Типо новая анкета',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.make_mark_keyboard(user_id),
                                                'attachment': 'photo' + owner_id + '_' + media_id})
                elif payload == '8':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Типо новая анкета',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.make_mark_keyboard(user_id),
                                                'attachment': 'photo' + owner_id + '_' + media_id})
                elif payload == '9':
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Типо закончил просмотр',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.main_keyboard.get_keyboard()})
            except KeyError:
                try:
                    vk.method('messages.send', {'user_id': user_id, 'message': 'Добро пожаловать',
                                                'random_id': random.randint(1, 1000),
                                                'keyboard': new_keyboards.first_keyboard.get_keyboard()})

                except Exception:
                    pass



if __name__ == '__main__':
    main()
