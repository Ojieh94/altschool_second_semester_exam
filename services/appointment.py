from fastapi import HTTPException

from schema import appointment
from schema.appointment import Appointments, AppointmentsCreate, AppointmentsEdit, AppointmentsStatus, appointments
from schema.doctor import AvailabilityStatus, Doctors, doctors
from schema.patient import patients
from utils.appointment import AppointmentHelpers



class AppointmentService:
    
    @staticmethod
    def parse_appointments(appointment_data):
        data = []
        for appointment in appointment_data:
            data.append(appointments[appointment])
        return data
    
    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        return appointment
    
    @staticmethod
    def create_appointment(payload: AppointmentsCreate):
        id = len(appointments)
        patient = patients.get(payload.patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found', status_code=404)
        doctor: Doctors = AppointmentHelpers.appoint_doctor_to_patient()

        appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
        )
        appointments[id] = appointment
        return appointment
    
    @staticmethod
    def edit_appointment(appointment_id: int, payload:AppointmentsEdit):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        
        if payload.patient_id != None:
            appointment.patient = patients.get(payload.patient_id)
            if appointment.patient is None:
                raise HTTPException(
                detail='Patient not found.', status_code=404
            )
        appointment.date = payload.date
        return appointment
    
    @staticmethod
    def delete_appointment(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        
        for doc, doctor in doctors.items():
            if doctor.name == appointment.doctor:
                doctor.is_available = AvailabilityStatus.TRUE
        
        del appointments[appointment_id]

    @staticmethod
    def complete_appointment(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        appointment.status = AppointmentsStatus.COMPLETED

        for doc, doctor in doctors.items():
            if doctor.name == appointment.doctor:
                doctor.is_available = AvailabilityStatus.TRUE
        return appointment
       



    