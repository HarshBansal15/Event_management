from datetime import datetime

class Venue:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} ({self.capacity})"


class Event:
    def __init__(self, id, name, datetime_str, venue, ticket_price):
        self.id = id
        self.name = name
        self.dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        self.venue = venue
        self.ticket_price = ticket_price

    @property
    def formatted_date(self):
        return self.dt.strftime("%d %b %Y %H:%M")

    def is_past(self):
        return self.dt < datetime.now()

    def __str__(self):
        return f"{self.name} @ {self.venue.name} | {self.formatted_date} | ₹{self.ticket_price}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.dt < other.dt

    def __hash__(self):
        return hash(self.id)


class FreeEvent(Event):
    def __init__(self, id, name, datetime_str, venue, registration_required=True):
        super().__init__(id, name, datetime_str, venue, 0)
        self.registration_required = registration_required

    def __str__(self):
        return super().__str__() + " | (FREE)"