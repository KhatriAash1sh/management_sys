import json

def load_students(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(file_path, students):
    with open(file_path, 'w') as file:
        json.dump(students, file, indent=4)

def add_student(file_path, student):
    students = load_students(file_path)
    students.append(student)
    save_students(file_path, students)
    print(f"Student {student['name']} added successfully.")




