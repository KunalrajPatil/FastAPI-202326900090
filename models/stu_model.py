from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    sem: int


class Student(BaseModel):
    id: int
    name: str
    email: str
    course: str
    sem: int