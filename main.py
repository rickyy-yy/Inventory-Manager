import os


def check_storage_files():
    product_file_path = r"C:\Users\yourf\Documents\Python\Inventory Manager\products.json"
    users_file_path = r"C:\Users\yourf\Documents\Python\Inventory Manager\users.json"

    if not os.path.isfile(product_file_path):
        product_file = open(product_file_path, 'x')
        product_file.close()

    if not os.path.isfile(users_file_path):
        users_file = open(users_file_path, 'x')
        users_file.close()


def is_user_valid(username, password):
    pass


def main_menu():
    print("=============================")
    print("Welcome to Inventory Manager!")
    print("=============================")
    print("")
    print("To proceed, you must login or register.")
    print("")
    print("1) Login")
    print("2) Register")
    print("3) Exit Program")
    print("")

    while True:
        try:
            user_choice = int(input("Enter your choice (1/2/3): "))
            print("")
            break
        except ValueError:
            print("")
            print("You must enter a number from 1 to 3.")
            print("")

    match user_choice:
        case 1:
            login_page()
        case 2:
            register_page()
        case 3:
            exit()
        case _:
            main_menu()


def login_page():
    print("=========================")
    print("Login Page")
    print("=========================")
    print("")
    user_username = str(input("Enter your username: "))
    user_password = str(input("Enter your password: "))
    print("")

    if is_user_valid(user_username, user_password):
        print("Login successful.")
        print("")
        selection_menu()
    else:
        print("Username/password is incorrect. Would you like to: ")
        print("1) Try again")
        print("2) Register")
        print("")

        while True:
            try:
                user_choice = int(input("Enter your choice (1/2): "))
                print("")
                break
            except ValueError:
                print("")
                print("You must enter a number from 1 to 2.")
                print("")

        match user_choice:
            case 1:
                login_page()
            case _:
                register_page()


def register_page():
    print("=========================")
    print("Register Page")
    print("=========================")
    print("")
    user_username = str(input("Enter your username: "))
    user_password = str(input("Enter your password: "))
    print("")


def selection_menu():
    pass


def create_product():
    pass


def edit_quantity():
    pass


def delete_product():
    pass


def load_product_data():
    pass


def save_product_data():
    pass


def sign_out():
    pass



if __name__ == '__main__':
    pass
    