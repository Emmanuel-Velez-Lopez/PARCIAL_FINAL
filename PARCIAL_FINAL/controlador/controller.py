# PARCIAL_FINAL/controlador/controller.py

import sys
sys.path.append("PROGRAMACION\\PARCIAL_FINAL\\model")

print(sys.path)

from model.doctor import Doctor
from model.hospital import Hospital

class HospitalController:
    def __init__(self):
        self.hospital = None

    def create_hospital(self, hospital_name):
        self.hospital = Hospital(hospital_name)

    def add_doctor(self, doctor_name, speciality, dni):
        if self.hospital:
            doctor = Doctor(doctor_name, speciality, dni)
            self.hospital.add_doctor(doctor)
        else:
            print("Error: Debe crear un hospital primero.")

    def search_by_dni(self, dni):
        if self.hospital:
            for doctor in self.hospital.doctors:
                if doctor.dni == dni:
                    return doctor, self.hospital
            return None, None
        else:
            print("Error: Debe crear un hospital primero.")
