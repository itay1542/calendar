

class Event:
    def __init__(self, name, location, datetime):
        self._name = name
        self._location = location
        self._datetime = datetime

    def get_date(self):
        return self._datetime.date()

    def __str__(self):
        return F"name: {self._name}, location: {self._location}, date and time: {self._datetime}"
