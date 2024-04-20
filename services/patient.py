from fastapi import HTTPException
from schema.patient import patients, Patients, PatientsCreate, PatientsEdit


class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for person in patient_data:
            data.append(patient_data[person])
        return data

    @staticmethod
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(
                detail='Patient does not exist.', status_code=404)
        return patient

    @staticmethod
    def create_patient(patient_data: PatientsCreate):
        id = len(patients)
        patient = Patients(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient
        return patient

    @staticmethod
    def edit_patient(patient_id: int, payload: PatientsEdit):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(
                detail='Patient does not exist.', status_code=404)

        if payload.name != None:
            patient.name = payload.name
        if payload.age != None:
            patient.age = payload.age
        if payload.sex != None:
            patient.sex = payload.sex
        if payload.weight != None:
            patient.weight = payload.weight
        if payload.height != None:
            patient.height = payload.height
        if payload.phone != None:
            patient.phone = payload.phone
        return patient

    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(
                detail='Patient does not exist.', status_code=404)
        del patients[patient_id]
