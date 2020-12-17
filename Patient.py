import json, time, os
from pathlib import Path


class Patient:
    def __init__(self, fname, lname, id, symptom):
        self._fname = fname
        self._lname = lname
        self._id = id
        self._symptom = symptom

    def patient_info(self):
        return f"First name: {self._fname} Last name: {self._lname} Symptom: {self._symptom} ID number: {self._id}"

    def update_symptom(self, new_symptom):
        self._symptom = new_symptom


p = Patient('Peter', 'Anteater', '111111', 'sick')
print(p.patient_info())
# print(Patient.patient_info(p))
p.update_symptom('more sick')
Patient.update_symptom(p, 'most sick')
p2 = Patient('Mark', 'Baldwin', '222222', 'ill')
print(p2.patient_info())
Patient.patient_info(p2)
