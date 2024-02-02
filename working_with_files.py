from csv import DictReader, DictWriter
from os.path import exists


class NameError:
    def __init__(self, txt):
        self.txt = txt


class PhoneError:
    def __init__(self, txt):
        self.txt = txt


def get_user_data():
    flag = False
    while not flag:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError("Невалидная длина!")
            second_name = input('Введите фамилию: ')
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) < 11:
                raise PhoneError("Неверная длина номера!")
            flag = True
        except ValueError:
            print('Вы вводите символы вместо цифр')
            continue
        except NameError as err:
            print(err)
            continue
        except PhoneError as err:
            print(err)
            continue
    return first_name, second_name, phone_number


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


file_name = 'phone.csv'
new_file = 'copy_phone.csv'


def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    user_data = get_user_data()
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(user_data[2]):
            print('Такой пользователь уже существует')
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Телефон': user_data[2]}
    res.append(obj)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_file(file_name, new_file):
    with open(file_name, encoding="utf-8", newline=""):
        list_1 = read_file(file_name)
        x = int(input(f'Введите номер строки (с 1 по {len(list_1)}), которую хотите скопировать: '))
        obj = list_1[x - 1]
        res = []
        res.append(obj)
        with open(new_file, "w", encoding="utf-8", newline="") as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)


def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print('Данные успешно записаны!')
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан, создайте его')
                continue
            print(read_file(file_name))
        elif command == 'c':
            if not exists(new_file):
                create_file(new_file)
            copy_file(file_name, new_file)
            print('Данные скопированы!')


main()
