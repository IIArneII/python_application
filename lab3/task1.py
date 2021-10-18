import re
from passwordError import *


def password(password):
    try:
        check_password(password)
    except PasswordError:
        return 'error'
    return 'ok'


def check_password(password):
    lit = {
        'й': 1, 'ц': 2, 'у': 3, 'к': 4, 'е': 5, 'н': 6, 'г': 7, 'ш': 8, 'щ': 9, 'з': 10, 'х': 11, 'ъ': 12,
        'ф': 14, 'ы': 15, 'в': 16, 'а': 17, 'п': 18, 'р': 19, 'о': 20, 'л': 21, 'д': 22, 'ж': 23, 'э': 24, 'ё': 25,
        'я': 27, 'ч': 28, 'с': 29, 'м': 30, 'и': 31, 'т': 32, 'ь': 33, 'б': 34, 'ю': 35,
        'q': 41, 'w': 42, 'e': 43, 'r': 44, 't': 45, 'y': 46, 'u': 47, 'i': 48, 'o': 49, 'p': 50,
        'a': 54, 's': 55, 'd': 56, 'f': 57, 'g': 58, 'h': 59, 'j': 60, 'k': 61, 'l': 62,
        'z': 67, 'x': 68, 'c': 69, 'v': 70, 'b': 71, 'n': 72, 'm': 73
    }

    if len(password) < 8:
        raise PasswordSizeError('Длина пароля меньше 8 символов')
    if not re.findall('\d', password):
        raise PasswordFormatError('Пароль не содержит цифры')
    if not re.findall('[A-ZА-Я]', password) or not re.findall('[a-zа-я]', password):
        raise PasswordFormatError('Пароль должен содержать буквы обоих регистров')
    pas = [password[i: i + 3].lower() for i in range(len(password) - 2)]
    for i in pas:
        if not re.findall('[^a-zа-я]', i):
            if lit[i[1]] - lit[i[0]] == 1 and lit[i[2]] - lit[i[1]] == 1:
                raise PasswordFormatError('Обнаружены тройка соседних на клавиатуре букв')


print(password('pa5Ffword'))
