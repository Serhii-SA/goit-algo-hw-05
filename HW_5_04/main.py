from pathlib import Path

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "You didn't attached the Name and phone nbr or attached too many arg-s.\nGive me name and phone please."
        except KeyError:
            nm = args[0]
            return print(f"No user with name - {nm[0]}")
    return inner

text= ''' 
"add username phone".

 За цією командою бот зберігає у пам'яті, 
новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.

"change username phone"
За цією командою бот зберігає в пам'яті новий номер телефону phone для 
контакту username, що вже існує в записнику.

"phone username"
 За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.

"all"
 За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.

"close", "exit"
 за будь-якою з цих команд бот завершує свою роботу
 '''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact with name {name} is already exists.If you'd like to change it, use command 'change'"
    #if 1<len(args)<3:
    else:    
        
        contacts[name] = phone
        return "Contact added."
    #else:
        #return "Invalid input"

@input_error
def chng_contact(args, contacts):
    #if 1<len(args)<3:
        name, phone = args
        contacts[name] = phone
        return f"Contact {name} phone number was changed(or added in case of not exists)."
    #else:
        #return "Invalid input"   
@input_error
def all_contact(contacts):
    if contacts == {}:
        print("\nContacts list is empty.\n")
    else:
        for key in contacts:
            print(key,contacts[key])

@input_error
def usn_ph(args, contacts):
    #try:
    return print(args[0],contacts[args[0]])
    #except:
        #print(f"No user with name - {args[0]}")
    
        
def main():
    contacts = {}
    try:
        fh = open("phonebook.txt","r")
        for line in fh:
            key, value = line.split()
            contacts[key.removesuffix(",")] = value
        #print(contacts)
        fh.close()
    except FileNotFoundError:
        print("\nFile with Phone Book doesn`t exist. If you go on,it will be created.\n")

    print("Welcome to the assistant bot!\n(\"Help\"-for help)")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            with open('phonebook.txt', 'w') as fh:
                for key, value in contacts.items():
                    fh.write(f'{key}, {value}\n')
            break



        elif command == "hello":
            print("How can I help you?(\"Help\"-for help)")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            all_contact(contacts)
        elif command == "change":
            print(chng_contact(args, contacts))
        elif command == "phone":
            usn_ph(args, contacts) 
        elif command == "help":
            print(text)           
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

