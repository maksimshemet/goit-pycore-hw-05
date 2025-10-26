import functools

def input_error(func):
    @functools.wraps(func)

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            if func.__name__ == "add_contact" or func.__name__ == "change_contact" and isinstance(e, IndexError):
                return "Give me name and phone please.\nExample - add John 1234567890 or change John 0987654321"
            elif func.__name__ == "get_contact":
                return "Contact not found."
            elif func.__name__ == "get_all":
                return "No contacts available."
            else:
                return "An error occurred. Please check your input."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def change_contact(args, contacts):

    name, phone = args
    if name not in contacts:
        print("Contact not found.")
        raise KeyError
    contacts[name] = phone
    return "Contact changed."

@input_error
def get_all(contacts):
    return contacts





def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
