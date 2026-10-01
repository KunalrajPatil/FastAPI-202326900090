from fastapi import APIRouter, HTTPException

from models.stu_model import Student, StudentCreate
from controllers import stu_controller

router= APIRouter()

@router.post('/students', response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    return stu_controller.create_student(student)

@router.get('/students',response_model=list[Student])
def get_students():
    return stu_controller.get_students()

@router.get('/students/{student_id}',response_model=Student)
def get_student(student_id: int):
    student = stu_controller.get_studentby_id(student_id)

    if student is None:
        raise HTTPException(status_code = 404, detail = 'Student not found')

    return student

@router.put('/students/{student_id}', response_model=Student)
def update_student(student_id: int, student: Student):
    updated_student = stu_controller.update_student(
        student_id,
        student
    )

    if updated_student is None:
        raise HTTPException(status_code=404, detail='Student not Found')

    return updated_student

@router.delete('/students/{student_id}', status_code=204)
def delete_student(student_id: int):
    deleted_student = stu_controller.delete_student(student_id)

    if deleted_student is None:
        raise HTTPException(status_code=404, detail='Student not found')

    