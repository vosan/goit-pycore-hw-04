def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args


def add_contact(args, contacts):
    assert len(args) == 2, "Invalid arguments count. Contact's name and phone are expected"

    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def change_contact(args, contacts):
    assert len(args) == 2, "Invalid arguments count. Contact's name and phone number are expected"

    name, _ = args
    if name not in contacts.keys():
        return "Contact not found."
    add_contact(args, contacts)
    return "Contact updated."


def show_phone(args, contacts):
    assert len(args) == 1, "Invalid arguments count. Only contact's name is expected"

    name = args[0]
    return contacts[name] if name in contacts else "Contact not found."


def output(message):
    print(f"\t{message}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            match command:
                case "close" | "exit" | "end" | "quit" | "stop":
                    output("Good bye!")
                    break
                case "hello" | "hi" | "hey":
                    output("How can I help you?")
                case "add":
                    output(add_contact(args, contacts))
                case "change" | "update":
                    output(change_contact(args, contacts))
                case "phone" | "get":
                    output(f"{show_phone(args, contacts)}")
                case "all":
                    if contacts:
                        output('=' * 30)
                        output("All Contacts:")
                        output('=' * 30)
                        for name, phone in contacts.items():
                            output(f"{name:.<20} {phone}")
                        output('=' * 30)
                    else:
                        output("No contacts available.")

                case _:
                    output(f"Invalid command.")

        except Exception as e:
            output(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
