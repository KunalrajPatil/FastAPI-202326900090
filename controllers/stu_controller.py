from models.stu_model import Student, StudentCreate

students = []

def create_student(student_data : StudentCreate):
    new_id = len(students) + 1

    student = Student(
        id = new_id,
        name= student_data.name,
        email= student_data.email,
        course= student_data.course,
        sem= student_data.sem
    )
    students.append(student)

    return student
    

def get_students():
    return students

def get_studentby_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    return None

def update_student(student_id: int,updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student

    return None

def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return deleted_student

    return None
    


