import json, time, os
from pathlib import Path

class Treatment(dict):
    """

    The treatment class have name and fee for each treatment. It also have how long each treatment take.

    """

    def __init__(self, treatment=None, fee=None, time=None):
        self.treatment = treatment
        self.fee = fee
        self.length = time

    def set_treatment(self, treatment, fee, time):
        self.treatment = treatment
        self.fee = fee
        self.length = time

    def get_treatment(self):
        return self.treatment


class Appointments:
    """
    The Appointments class exposes the properties required to create an appointment. We use this class to manage
    information regarding to appointments. An Appointments class should ensure that it has
    - appointment number
    - time
    of appointment - patient name or code - room number: We have rooms: 101, 102, 103, 201, 202, 203.
    - treatment: Tooth Filling, Cap	,Root Canals, Tooth Removal, Early Gum Disease, Gum Surgery, Braces, Bone Surgery,
    Removable Bridge, Teeth Cleaning, X-Rays, Deep Cleaning. - fee


    """

    def __init__(self, app_number, app_time, patient):
        self.app_number = app_number  # REQUIRED
        self.app_time = app_time  # REQUIRED
        self.patient = patient  # REQUIRED
        self.room = 'unknown'  # OPTIONAL
        self.fee = ''  # OPTIONAL
        self.__treatment = []  # OPTIONAL

    """

    add_post accepts a Post object as parameter and appends it to the posts list. Posts are stored in a list object 
    in the order they are added. So if multiple Posts objects are created, but added to the Profile in a different 
    order, it is possible for the list to not be sorted by the Post.timestamp property. So take caution as to how you 
    implement your add_post code. 

    """

    def add_treatment(self, treatment: Treatment) -> None:
        self.__treatment.append(treatment)

    """

    del_treatment removes a Treatment.

    """

    def del_treatment(self, index: int) -> bool:
        try:
            del self.__treatment[index]
            return True
        except IndexError:
            return False

    """

    del_treatment list of Treatments

    """

    def list_treatment(self) -> list:
        return self.__treatment

    """

    save_profile accepts an existing dsu file to save the current instance of Profile to the file system.

    Example usage:

    profile = Profile()
    profile.save_profile('/path/to/file.dsu')

    Raises DsuFileError

    """

    def save_appointment(self, path: str) -> None:
        p = Path(path)

        if os.path.exists(p) and p.suffix == '.dsu':
            try:
                f = open(p, 'w')
                json.dump(self.__dict__, f)
                f.close()
            except Exception as ex:
                raise ex
        else:
            raise Exception("file does not exist!")

    """

    load_profile will populate the current instance of Profile with data stored in a DSU file.

    Example usage: 

    profile = Profile()
    profile.load_profile('/path/to/file.dsu')

    Raises DsuProfileError, DsuFileError

    """

    def load_appointment(self, path: str) -> None:
        p = Path(path)

        if os.path.exists(p) and p.suffix == '.app':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.bio = obj['bio']
                for post_obj in obj['_Profile__posts']:
                    post = Post(post_obj['entry'])
                    post.timestamp = post_obj['timestamp']
                    self.add_post(post)
                f.close()
            except Exception as ex:
                raise ex
        else:
            raise DsuFileError()
