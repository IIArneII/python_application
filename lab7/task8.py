import sqlite3
import random
from unittest.mock import Mock, patch


def get_name(cursor: sqlite3.Cursor):
    data = cursor.execute('SELECT name from items').fetchall()
    data = list(map(lambda x: x[0], data))
    return random.choice(data)


def test_mock_get_name_1():
    expected = 'Телефон'

    cursor = Mock()
    fetchall = Mock(return_value=[('Телефон',), ('Соковыжималка',), ('Телевизор',), ('Холодильник',)])
    execute = Mock(return_value=cursor)
    cursor.fetchall = fetchall
    cursor.execute = execute

    def new_choice(data):
        return data[0]

    with patch('random.choice', new_choice):
        assert get_name(cursor) == expected


def test_mock_get_name_2():
    expected = 'Соковыжималка'

    cursor = Mock()
    fetchall = Mock(return_value=[('Телефон',), ('Соковыжималка',), ('Телевизор',), ('Холодильник',)])
    execute = Mock(return_value=cursor)
    cursor.fetchall = fetchall
    cursor.execute = execute

    def new_choice(data):
        return data[1]

    with patch('random.choice', new_choice):
        assert get_name(cursor) == expected


def test_mock_get_name_3():
    expected = 'Телевизор'

    cursor = Mock()
    fetchall = Mock(return_value=[('Телефон',), ('Соковыжималка',), ('Телевизор',), ('Холодильник',)])
    execute = Mock(return_value=cursor)
    cursor.fetchall = fetchall
    cursor.execute = execute

    def new_choice(data):
        return data[2]

    with patch('random.choice', new_choice):
        assert get_name(cursor) == expected


if __name__ == '__main__':
    db = sqlite3.connect('task8.db')
    cursor = db.cursor()
    print(get_name(cursor))
