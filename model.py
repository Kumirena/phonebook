def read_phonebook():

    with open('file.txt', 'r+', encoding='utf-8') as file:
        line = file.readlines()
        list = []
        return list
        print(line)


def find():
    surname = input('Введите фамилию:')
    print('В справочнике найдено: ')
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
    count = 0
    for i in s:
        if surname in i:
            print(i, sep="\n")
            count += 1
    if count == 0:
        return
       # print('К сожалению, контакт не найден')


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию:')
    phone = input('Введите номер телефона: ')
    with open('file.txt', 'a+', encoding='utf-8') as file:
        file.write(name + ' ')
        file.write(surname + ' ')
        file.write(phone + ' ')
    file.close()


def delete_contact():
    surname = input('Введите фамилию контакта, который хотите удалить:')
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        for i in range(0, len(s)-1):
            if surname in s[i]:
                s.pop(i)
    file.close()


def edit_contact():
    surname = input('Введите фамилию контакта, который хотите изменить:')
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        for i in range(0, len(s)):
            if surname in s[i]:
                s[i] = input("Введите новые данные: ") + "\n"
    non_empty_lines = (i for i in s if not i.isspace())
    with open('file.txt', 'w', encoding='utf-8') as file_1:
        file_1.writelines(i for i in non_empty_lines)
    file.close()
