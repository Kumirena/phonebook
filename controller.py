import view
import model
def run():
    view.greetings()
    while True:
        view.menu()
        answer = input('')
        if answer == '1':
            data = model.read_phonebook()
            view.read_phonebook(data)        
        elif answer == '2':
            data = model.find()
            #view.find()                    
        elif answer == '3':
            data = model.add_contact()
            #view.add_contact()                   
        elif answer == '4':
            data = model.delete_contact()
            #view.delete_contact()                     
        elif answer == '5':
            data = model.edit_contact()
            #view.edit_contact()           
        elif answer == '6':
            break
            #data = model.quit_contact()
            #view.quit_contact()