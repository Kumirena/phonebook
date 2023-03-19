def read_phonebook():  

   with open('file.txt', 'r+', encoding= 'utf-8') as file:
        s = file.readlines()
        list = []
        return list
   
def find():
    surname = input('Введите фамилию контакта: ')
    print('В справочнике найдено: ')
    with open('file.txt', 'r+', encoding= 'utf-8') as file:
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
    surname = input('Введите фамилию:')
    phone = input('Введите номер телефона: ')
    with open('file.txt', 'a+', encoding= 'utf-8') as file:
        file.write(name + ' ')
        file.write(surname + ' ')
        file.write(phone + ' ')
    print(f'Контакт {surname} добавлен, спасибо!')