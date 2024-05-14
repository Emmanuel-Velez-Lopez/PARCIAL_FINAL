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