from phoneError import *
import re


def check_phone(phone):
    if phone.count('(') > 1 or phone.count(')') > 1 or phone.count('(') != phone.count(')'):
        raise FormatError('Неверный формат')
    f = phone.find('(')
    if f != -1 and phone[f + 1:].find(')') == -1:
        raise FormatError('Неверный формат')

    if re.findall('- *-', phone) or re.findall('^-', phone) or re.findall('-$', phone) or \
            re.findall('[^\d()\-+ ]+', phone):
        raise FormatError('Неверный формат')

    if len(re.findall('\d', phone)) != 11:
        raise CountError('Неверное количество цифр')

    if phone[0: 2] != '+7' and phone[0] != '8':
        raise CodeError('Неверный код страны')

    new_phone = re.sub('[^+\d]', '', phone)
    new_phone = re.sub('^8', '+7', new_phone)

    p = 1
    if new_phone[0] == '+':
        p = 2
    p = new_phone[p: p + 3]

    s = list(range(910, 920)) + list(range(980, 990)) + list(range(920, 940)) + list(range(902, 907)) + list(
        range(960, 970))
    if int(p) not in s:
        raise OperatorError('Не определяется оператор сотовой связи')

    return new_phone

if __name__ == '__main__':
    try:
        print(check_phone('8(916) 12 4 32-6 7'))
    except FormatError as e:
        print(e)
    except CountError as e:
        print(e)
    except CodeError as e:
        print(e)
    except OperatorError as e:
        print(e)
