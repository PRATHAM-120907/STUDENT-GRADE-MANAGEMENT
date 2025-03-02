students = []

def student():
    student_information = {
        "name": input("ENTER THE NAME: "),
        "age": int(input("ENTER THE AGE: ")),
        "class": int(input("ENTER THE CLASS: ")),
        "total_marks": int(input("ENTER TOTAL MARKS OF ALL SUBJECTS: ")),
    }
    return student_information

def add_student():
    student_info = student()
    students.append(student_info)
    print("Student information saved successfully!")

def get_student_info(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

while True:
    add_student()
    more_students = input("DO YOU WANT TO ADD MORE STUDENTS? (YES/NO): ").strip().lower()
    if more_students != 'yes':
        break

while True:
    search_name = input("ENTER THE NAME OF THE STUDENT TO GET INFORMATION (or type 'exit' to quit): ").strip()
    if search_name.lower() == 'exit':
        break
    student_info = get_student_info(search_name)
    if student_info:
        print(student_info)
    else:
        print("Student not found.")

