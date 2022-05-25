from datetime import datetime
from event_store import *
from event_actions import *

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
ACTION_CHOICES = {
    'see_events': EventActions.SEE_EVENTS,
    'add_event': EventActions.ADD_EVENT,
}


class EventCalendar:
    def __init__(self):
        self.store = EventStore()

    def run(self):
        while True:
            action_choice = input("select action (%s) ---> "
                                  % [F"{key}" for key in ACTION_CHOICES.keys()])
            if not action_choice in ACTION_CHOICES.keys():
                print("invalid input, please choose one of the printed options")
            else:
                self._operate_action(ACTION_CHOICES[action_choice])
            self.store.remove_old()

    def _operate_action(self, choice):
        if choice == EventActions.SEE_EVENTS:
            for event in self.store.get_events():
                print("- %s" % event)
        elif choice == EventActions.ADD_EVENT:
            event = self.__input_event()
            self.store.add_event(event)
            print("event added successfully")

    def __input_event(self):
        name = input("insert name ---> ")
        date = None
        location = input("insert location ---> ")
        while date == None:
            try:
                date = datetime.strptime(input("insert date and time (%s) ---> " % DATETIME_FORMAT), DATETIME_FORMAT)
            except ValueError as e:
                print(e)
                print("invalid datetime input, try again:")
                date = None
        return Event(name, location, date)
