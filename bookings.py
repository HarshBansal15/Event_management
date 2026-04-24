class OverbookingError(Exception):
    pass


class Booking:
    counter = 1

    def __init__(self, customer, event, num_tickets):
        self.customer = customer
        self.event = event
        self.num_tickets = num_tickets
        self.booking_id = f"BK{str(Booking.counter).zfill(3)}"
        Booking.counter += 1
        self.total_price = event.ticket_price * num_tickets

    def __str__(self):
        return f"{self.booking_id} - {self.customer} - {self.event.name} - {self.num_tickets} tickets"


class BookingEngine:
    def __init__(self):
        self.event_seats = {}  
        self.bookings = {}
        self.waiting_list = {}

    def book(self, customer, event, qty):
        seats_booked = self.event_seats.get(event, 0)

        if seats_booked + qty > event.venue.capacity:
            self.waiting_list.setdefault(event, []).append((customer, qty))
            raise OverbookingError("Not enough seats!")

        booking = Booking(customer, event, qty)
        self.bookings[booking.booking_id] = booking  
        self.event_seats[event] = seats_booked + qty

        return booking

    def cancel(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings.pop(booking_id)  
            self.event_seats[booking.event] -= booking.num_tickets

    def seats_left(self, event):
        return event.venue.capacity - self.event_seats.get(event, 0)

    def is_sold_out(self, event):
        return self.seats_left(event) == 0

    def customer_bookings(self, name):
        return [b for b in self.bookings.values() if b.customer == name]