#OOP Principles

class Patient:
    def __init__(self, name, age): # This demonstrates Encapsulation
        self.name = name
        self.age = age

    #Getters and Setters
    def get_name(self):
        return self.name   

    def get_age(self):
        return self.age 
    
    def set_name(self, name):
        if type(name) == str:       
            self.name = name
    
    def set_age(self, age):
        if type(age) == int:         
            self.age = age 

    def display_status(self):
        return "Patient: {} - Admitted".format(self.name) 

# This demonstrates Inheritance:
class InPatient(Patient):
    room_number = None  # Default 
    def set_room_number(self, room_number):
        self.room_number = room_number

class DischargedPatient(Patient):
    discharge_date = None  # Default 
    def set_discharge_date(self, discharge_date):
        self.discharge_date = discharge_date

    next_appointment = None
    def set_next_appointment(self, next_appointment):
        self.next_appointment = next_appointment

class EmergencyInPatient(InPatient): #inherits InPatient subclass
    in_date = None  # Default 
    def set_in_date(self, in_date):
        self.in_date = in_date

    #This demonstrates Polymorphism-method overriding   
    def get_age(self):
        if type(self.age) == int:
            if self.age < 18:
                return "Minor"
            else:
                return self.age

    def display_status(self):
        return "Emergency Inpatient: {} - Not Admitted".format(self.name)    

#This demonstrates Abstraction
class PatientRoster:
    def __init__(self):
        self.patients = []

    def add_new_patient(self, name, age):
        patient = Patient(name, age)
        self.patients.append(patient)

    def remove_patient_by_name(self, name):
        for patient in self.patients:
            if patient.get_name() == name:
                self.patients.remove(patient)

#Test:

# Encapsulation
patient0 = Patient("Duaa", 23)
print(patient0.get_name())  
print(patient0.get_age())   
patient0.set_name("Shay")
patient0.set_age(14)
print(patient0.get_name())  
print(patient0.get_age())

#Inheritance
patient1 = InPatient("Bob", 32)
patient1.set_room_number(109)
print(patient1.room_number)
print(patient1.display_status()) 

patient2 = DischargedPatient("John", 64)
patient2.set_discharge_date("2024-05-15")
patient2.set_next_appointment("2024-06-01")
print(patient2.next_appointment)

#Polymorphism
baby1 = EmergencyInPatient("Aayra", 2)
baby1.set_in_date("2024-05-15")
print(baby1.get_age())
print(baby1.display_status())

#Abstraction
roster = PatientRoster()
roster.add_new_patient("Rachel", 50)
roster.add_new_patient("Holly", 12)      
roster.remove_patient_by_name("Rachel")
for patient in roster.patients:
    print(patient.name)