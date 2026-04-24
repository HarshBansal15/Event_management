from models import Venue, Event
from booking import BookingEngine, OverbookingError
from analytics import *

# Data
events_data = [
    ("EVT01", "Coldplay Concert", "2025-03-15 19:00", "Arena A", 100, 2500),
    ("EVT02", "Python Summit", "2025-03-15 10:00", "Hall B", 50, 800),
    ("EVT03", "Art Exhibition", "2025-03-20 11:00", "Gallery C", 30, 400),
    ("EVT04", "Stand-up Night", "2025-03-22 20:00", "Arena A", 80, 1200),
]

bookings_raw = [
    ("alice", "EVT01", 2),
    ("bob", "EVT01", 1),
    ("alice", "EVT02", 1),
    ("charlie", "EVT03", 3),
    ("bob", "EVT02", 2),
    ("dave", "EVT01", 5),
    ("charlie", "EVT04", 2),
]

# Create events
venues = {}
events = {}

for id, name, dt, venue_name, cap, price in events_data:
    if venue_name not in venues:
        venues[venue_name] = Venue(venue_name, cap)
    events[id] = Event(id, name, dt, venues[venue_name], price)

# Booking engine
engine = BookingEngine()
all_bookings = []

for customer, eid, qty in bookings_raw:
    try:
        b = engine.book(customer, events[eid], qty)
        all_bookings.append(b)
    except OverbookingError:
        pass

# Analytics
report = revenue_report(events, all_bookings)
top = top_event(report, events)
total = total_revenue(report)
spend = customer_spend(all_bookings)
vip = vip_customers(spend)
daily = daily_revenue(all_bookings)

# Output
print("Revenue Report:", report)
print("Top Event:", top)
print("Total Revenue:", total)
print("Customer Spend:", spend)
print("VIP Customers:", vip)
print("Daily Revenue:", daily)
print("Seats Left EVT1:", engine.seats_left(events["EVT01"]))