def read_phonebook():  

   with open('file.txt', 'r+', encoding= 'utf-8') as file:
        s = file.readlines()
        list = []
        return list