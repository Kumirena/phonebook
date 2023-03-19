def read_phonebook():

    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        list = []
        return list


def find():
    surname = input('Введите фамилию контакта: ')
    print('В справочнике найдено: ')
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
    count = 0
    for i in s:
        if surname in i:
            print(i, sep="\n")
            count += 1
    if count == 0:
        print('К сожалению, контакт не найден')
        return


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    with open('file.txt', 'a+', encoding='utf-8') as file:
        new_contact = name + ' ' + surname + ' ' + phone
        file.write("%s\n" % new_contact)
        file.close()


def delete_contact():
    delete_contact = input(
        'Введите фамилию контакта, который хотите удалить: ')
    delete_contact = delete_contact.lower()
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        s = [line for line in s if delete_contact not in line.lower()]
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.writelines(s)
        # for i in range(len(s)):
        # if s[i]["name"] == delete_contact:
        # del s[i]
        # break
        # s.pop(i)
    file.close()


def edit_contact():
    surname = input('Введите фамилию контакта, который хотите изменить: ')
    with open('file.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        for i in range(len(s)):
            if surname in s[i]:
                s[i] = input(
                    'Введите новые фамилию, имя и номер телефона: ') + '\n'
    non_empty_lines = (i for i in s if not i.isspace())
    with open('file.txt', 'w', encoding='utf-8') as file_1:
        file_1.writelines(i for i in non_empty_lines)
    file.close()
