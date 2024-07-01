# In-memory user storage (for demonstration purposes only)

users = {}

def register_user(username, password):
    if username in users:
        print("User already exists.")
        return False
    else:
        users[username] = password
        print("User registered successfully.")
        return True

def login_user(username, password):
    if username not in users:
        print("User does not exist.")
        return False
    else:
        if users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
            return False

# Example usage
if __name__ == "__main__":
    while True:
        choice = input("Do you want to register or login? (register/login/exit): ").strip().lower()
        if choice == "register":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(username, password)
        elif choice == "login":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login_user(username, password)
        elif choice == "exit":
            break
        else:
            print("Invalid choice, please enter 'register', 'login', or 'exit'.")
