from users_management import UsersManager

MAIN_MENU_OPTIONS = {
    1: "Login",
    2: "Register"
}

def display_main_menu():
    print("\nWELCOME to the Terminal Chat Room App!\n")
    print("Please Choose what do you want to do from the list below by entering the appropiate number (1, 2 ...)")
    for option in MAIN_MENU_OPTIONS:
        print(f"\t{option}. {MAIN_MENU_OPTIONS[option]}")

def get_user_choice():

    while True:
        try:
            choice = int(input()) # Get user choice
        except ValueError:
            print("Your input must be an integer!")
            continue
        
        if choice not in MAIN_MENU_OPTIONS:
            first_option = min(MAIN_MENU_OPTIONS, key=MAIN_MENU_OPTIONS.get)
            last_option = max(MAIN_MENU_OPTIONS, key=MAIN_MENU_OPTIONS.get)
            print(f"Choose integer between {first_option} and {last_option} inclusive!")
            continue

        return choice

def start():

    display_main_menu() # Display Main Menu options to the user

    user_choice = get_user_choice()

    users_manager = UsersManager()

    while True:
        if user_choice == 1:
            try:
                users_manager.login()
            except ValueError as e:
                print(e)

        elif user_choice == 2:
            try:
                users_manager.register()
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    start()
