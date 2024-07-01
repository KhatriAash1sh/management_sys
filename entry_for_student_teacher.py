from .file_read_write_append import*


def file_operation():
    file_path="data.json"
    while True:
        choice = input("Do you want to read, write, or append a student? (read/write/append/exit): ")
        
        if choice == 'read':
            students = load_students(file_path)
            print(json.dumps(students, indent=4))
        
        elif choice == 'write':
            students = []
            num_students = int(input("How many students do you want to add? "))
            for _ in range(num_students):
                name = input("Enter student name: ")
                roll_no = input("Enter student roll number: ")
                phone = input("Enter student phone number: ")
                email = input("Enter student email: ")
                student = {"name": name, "roll_no": roll_no, "phone": phone, "email": email}
                students.append(student)
            save_students(file_path, students)
            print("Students data written successfully.")
        
        elif choice == 'append':
            name = input("Enter student name: ")
            roll_no = input("Enter student roll number: ")
            phone = input("Enter student phone number: ")
            email = input("Enter student email: ")
            student = {"name": name, "roll_no": roll_no, "phone": phone, "email": email}
            add_student(file_path, student)
        
        elif choice == 'exit':
            break
        
        else:
            print("Invalid choice, please enter 'read', 'write', 'append', or 'exit'.")
if __name__ == "__main__":
   file_operation()