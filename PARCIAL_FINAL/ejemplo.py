# Importa las clases necesarias
from model.hospital import Hospital
from model.doctor import Doctor
from controlador.controller import HospitalController

# Crea una instancia del controlador del hospital
hospital_controller = HospitalController()

# Crea un hospital
hospital_controller.create_hospital("Hospital General")

# Agrega algunos médicos
hospital_controller.add_doctor("John Smith", "Cardiología", "12345678A")
hospital_controller.add_doctor("Alice Johnson", "Pediatría", "87654321B")
hospital_controller.add_doctor("Michael Brown", "Neurología", "98765432C")

# Busca un médico por su DNI
dni = "87654321B"
doctor, hospital = hospital_controller.search_by_dni(dni)
if doctor and hospital:
    print("Doctor encontrado:")
    print("Nombre:", doctor.doctor_name)
    print("Especialidad:", doctor.speciality)
    print("Hospital:", hospital.hospital_name)
else:
    print("Doctor no encontrado.")

# PARCIAL_FINAL/GUI/main.py

import sys
sys.path.append("PROGRAMACION\\PARCIAL_FINAL\\controlador")

print(sys.path)

import tkinter as tk
from tkinter import messagebox
from controlador.controller import HospitalController 

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Información Hospitalaria")
        self.geometry("600x400")

        self.controller = HospitalController()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Buscar Doctor por DNI:")
        self.label.pack()

        self.dni_entry = tk.Entry(self)
        self.dni_entry.pack()

        self.search_button = tk.Button(self, text="Buscar", command=self.search_by_dni)
        self.search_button.pack()

    def search_by_dni(self):
        dni = self.dni_entry.get()
        doctor, hospital = self.controller.search_by_dni(dni)
        if doctor and hospital:
            messagebox.showinfo("Doctor encontrado", f"Doctor: {doctor.doctor_name}\nEspecialidad: {doctor.speciality}\nHospital: {hospital.hospital_name}")
        else:
            messagebox.showerror("Error", "Doctor no encontrado.")

# Ejecuta la aplicación
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
