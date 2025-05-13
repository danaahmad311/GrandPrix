from models.ticket import Ticket, save_tickets

sample_tickets = [
    Ticket("T1", "Single Race Pass", 100.0, "1 Day", "Access to one race event"),
    Ticket("T2", "Weekend Package", 250.0, "3 Days", "Access to weekend races and pit walk"),
    Ticket("T3", "Season Membership", 1500.0, "All Season", "All races + VIP access"),
    Ticket("T4", "Group Discount", 80.0, "1 Day", "Group of 5 or more"),
]

save_tickets(sample_tickets)
print("Tickets initialized successfully.")
