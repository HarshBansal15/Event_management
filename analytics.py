def revenue_report(events, bookings):
    report = {}
    for b in bookings:
        eid = b.event.id
        report[eid] = report.get(eid, 0) + b.total_price
    return report


def top_event(report, event_lookup):
    top_id = max(report, key=report.get)
    return event_lookup[top_id].name


def total_revenue(report):
    return sum(report.values())


def customer_spend(bookings):
    spend = {}
    for b in bookings:
        spend[b.customer] = spend.get(b.customer, 0) + b.total_price
    return spend


def vip_customers(spend):
    return [k for k, v in spend.items() if v > 5000]


def daily_revenue(bookings):
    daily = {}
    for b in bookings:
        date = b.event.dt.strftime("%Y-%m-%d")
        daily[date] = daily.get(date, 0) + b.total_price
    return dict(sorted(daily.items(), key=lambda x: x[1], reverse=True))