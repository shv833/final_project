from Bot import *


if __name__ == "__main__":
    print("Hello. I am your contact-assistant. What should I do with your contacts?")

    choice = {
        "add": AddBot(),
        "search": SearchBot(),
        "edit": EditBot(),
        "remove": RemoveBot(),
        "save": SaveBot(),
        "load": LoadBot(),
        "congratulate": CongratulateBot(),
        "view": ViewBot(),
        "exit": ExitBot(),
    }

    while True:
        action = (
            input("Type help for list of commands or enter your command\n")
            .strip()
            .lower()
        )

        if action == "help":
            format_str = str("{:%s%d}" % ("^", 20))
            for command in choice:
                print(format_str.format(command))

        if action in choice:
            choice[action].handle()
            if action in ["add", "remove", "edit"]:
                book.save("auto_save")
        else:
            print("Incorrect option")
