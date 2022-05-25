from event import *
from datetime import date


class EventStore:

    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def get_events(self, date = date.today()):
        return list(filter(lambda event: event.get_date() == date, self.events))

    def remove_old(self):
        today = date.today()
        self.events = list(filter(lambda event: event.get_date() >= today, self.events))