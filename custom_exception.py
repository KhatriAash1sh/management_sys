#No_matching_name_Error_Handling
#No_matching_Id_Error
#Authentical_Error


def find_name(name, names_list):
    if name not in names_list:
        raise teacher(f"No matching name found for: {name}")

def find_id(id, ids_list):
    if id not in ids_list:
        raise NoMatchingIdError(f"No matching ID found for: {id}")

def authenticate(student_name, password):
    # Assume a dummy authentication function
    if user != "admin" or password != "adminpass":
        raise AuthenticalError("Authentication failed.")

try:
    # Example usage
    names = ["Alice", "Bob", "Charlie"]
    ids = [1, 2, 3]
    
    find_name("David", names)
    find_id(4, ids)
    authenticate("user", "wrongpass")

except NoMatchingNameErrorHandling as e:
    print(e)
except NoMatchingIdError as e:
    print(e)
except AuthenticalError as e:
    print(e)
else:
    print("All operations succeeded without exceptions.")
finally:
    print("Operation completed.")
