from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel

from schema.doctor import doctors
from schema.patient import Patients, patients


class AppointmentsStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    

class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: str
    date: date
    status: AppointmentsStatus = AppointmentsStatus.PENDING


class AppointmentsCreate(BaseModel):
    patient_id: int
    date: date

class AppointmentsEdit(BaseModel):
    patient_id: Optional[int] = None
    date: date
    


appointments: dict[int, Appointments] = {
    0: Appointments(
    id=0, patient=patients[0], doctor=doctors[0].name, date=date(2024, 3, 19)
)
}
