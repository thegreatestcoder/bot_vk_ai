from vk_api import keyboard
from vk_api.keyboard import VkKeyboardColor

pre_start_keyboard = keyboard.VkKeyboard(one_time=False)
pre_start_keyboard.add_button('Начать', color=VkKeyboardColor.POSITIVE, payload='{"command":"start"}')

first_keyboard = keyboard.VkKeyboard(one_time=False)
first_keyboard.add_button('Получить аватар', color=VkKeyboardColor.POSITIVE, payload='1')
first_keyboard.add_button('Описание', color=VkKeyboardColor.PRIMARY, payload='10')

main_keyboard = keyboard.VkKeyboard(one_time=False)
main_keyboard.add_button('Показать аватар', color=VkKeyboardColor.SECONDARY, payload='2')
main_keyboard.add_line()
main_keyboard.add_button('Cоздать новый аватар', color=VkKeyboardColor.PRIMARY, payload='3')
main_keyboard.add_line()
main_keyboard.add_button('Cмотреть анкеты', color=VkKeyboardColor.POSITIVE, payload='4')

payment_keyboard = keyboard.VkKeyboard(one_time=False)
payment_keyboard.add_vkpay_button(hash='amount=1&description=Новый аватар&action=pay-to-group&group_id=202174461',
                                  payload='5')
payment_keyboard.add_line()
payment_keyboard.add_button('Отмена', color=VkKeyboardColor.SECONDARY, payload='6')


def make_mark_keyboard(profile_id):
    mark_keyboard = keyboard.VkKeyboard(one_time=False)
    mark_keyboard.add_button('Нравится', color=VkKeyboardColor.POSITIVE, payload=f'7{profile_id}')
    mark_keyboard.add_button('Не нравится', color=VkKeyboardColor.NEGATIVE, payload='8')
    mark_keyboard.add_line()
    mark_keyboard.add_button('Закончить просмотр', color=VkKeyboardColor.SECONDARY, payload='9')
    return mark_keyboard.get_keyboard()
