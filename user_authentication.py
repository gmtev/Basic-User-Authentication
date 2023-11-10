users_credentials = {}
users_data = {}


def register():
    print("Register a new user:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    email = input("Enter your e-mail:")
    if username in users_credentials:
        print("Username already exists. Please choose a different one.")
    else:
        users_credentials[username] = password
        users_data[username] = [name, email]
        print("Registration successful!")


def login():
    print("Login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_credentials and users_credentials[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return False


def view_profile(username):
    print(f"Profile for {username}:")
    print(f"Your name is: {users_data[username][0]}")
    print(f"Your e-mail is: {users_data[username][1]}")


def change_data(username):
    print("What would you like to change?\n1. Password\n2. Name\n3. E-mail")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        new_password = input("Enter your new password: ")
        users_credentials[username] = new_password
    elif choice == "2":
        new_name = input("Enter your new name: ")
        users_data[username][0] = new_name
    elif choice == "3":
        new_email = input("Enter your new e-mail: ")
        if new_email not in users_data.values():
            users_data[username][1] = new_email
        else:
            print("Email is already taken!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


logged_in = False
current_user = ''
while True:
    if not logged_in:
        print("Welcome to the User Authentication System!:\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            register()
        elif choice == '2':
            current_user = login()
            if current_user:
                logged_in = True
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Welcome to your profile!\n1. View profile\n2. Change your data\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            view_profile(current_user)
        elif choice == "2":
            change_data(current_user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")