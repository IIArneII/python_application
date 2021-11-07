import hashlib
import secrets


def get_hash_password(password):
    salt = secrets.randbits(256).to_bytes(32, 'big')
    h = hashlib.scrypt(password, salt=salt, n=8, r=256, p=4, dklen=32)
    return h, salt


def check_password(password, hash, salt):
    h = hashlib.scrypt(password, salt=salt, n=8, r=256, p=4, dklen=32)
    return hash == h


if __name__ == '__main__':
    line = -1
    while line != 0:
        line = int(input('0 - Выход\n1 - Регистрация\n2 - Вход\n'))
        if line == 1:
            login = input('\nЛогин: ')
            password = input('Пароль: ')
            h, salt = get_hash_password(password.encode())
            f = open('passwords.txt', 'ab')
            f.write(login.encode() + b'\n' + h + b'\n' + salt + b'\n')
            f.close()

        if line == 2:
            login = input('\nЛогин: ')
            password = input('Пароль: ')
            f = open('passwords.txt', 'rb')
            l = f.readlines()
            for i in range(0, len(l), 3):
                if login.encode() == l[i][0: -1] and check_password(password.encode(), l[i+1][0: -1], l[i+2][0: -1]):
                    print('Удачно')
