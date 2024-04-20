from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True


class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorsEdit(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None


doctors: dict[int, Doctors] = {
    0: Doctors(id=0, name='Dr. Adeshina Wale', specialization='Surgeon', phone='08012345678', is_available=False),
    1: Doctors(id=1, name='Dr. Ngozi Ada', specialization='Optician', phone='07012356798'),
    2: Doctors(id=2, name='Dr. Hassan Usman', specialization='Gynaecology', phone='07056489321')

}
