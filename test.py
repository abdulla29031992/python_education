def choice_action(phonebook):
    while True:
        print("what do you want?")
        user_choice = input('1 - import data\n2 - search contact\n3 - add contact/n4 - change contact\
                            n5 - delete contact/n6 - show contact\n0 - quit the application\n')
        print()
        if user_choice == '1':
            file_to_add = input("enter the name of import data")
            import_data(file_to_add, phonebook)
        if user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        if user_choice == '3':
            add_phone_number(phonebook)
        if user_choice == '4':
            change_phone_number(phonebook)
        if user_choice == '5':
            delete-contact(phonebook)
        if user_choice == '6':
            show_phonebook(phonebook)
        if user_choice == '0':
            print('bye')
            break
        else:
            print("Incorrectly entered command")
            continue

def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding= 'utf-8') as new_contact open(phonebook, 'a', encoding= 'utf-8') as file:
            contact_to_add = new_contact.readlines()
            file.writelines(contact_to_add)
    except FileNotFoundError:
        print(f"{file_to_add} not found")

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding= 'utf-8') as file:
        lines = line.readlines()
    headers = ['last name', 'name', 'number of phone']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
        return contact_list
    
def read_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8'):
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
            return contact_list    

