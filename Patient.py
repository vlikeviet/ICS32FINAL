import json, time, os
from pathlib import Path


class Patient:
    def __init__(self, fname=None, lname=None, id=None, symptom=None):
        self._fname = fname
        self._lname = lname
        self._id = id
        self._symptom = symptom

    def patient_info(self):
        return f"First name: {self._fname} Last name: {self._lname} Symptom: {self._symptom} ID number: {self._id}"

    def update_symptom(self, new_symptom):
        self._symptom = new_symptom

    def save_patient(self, path):
        p = Path(path)

        if os.path.exists(p) and p.suffix == '.pat':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as ex:
                raise ex
        else:
            raise Exception("File does not exist!")
