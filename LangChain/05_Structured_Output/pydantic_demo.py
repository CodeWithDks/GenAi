from pydantic import BaseModel,Field,EmailStr
from typing import Optional,Literal

class Student(BaseModel):
    name: str
    age: int
    city: Optional[str] = 'Patna'
    gender: str = Literal['f','m']
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student.')
    email: EmailStr


new_student = {
    'name':'Radah',
    'age':21,
    'gender':'f',
    'cgpa': 8,
    'email':'radha@gmail.com'
}

student1 = Student(**new_student)

student_dict = dict(student1)

print(student_dict['city'])