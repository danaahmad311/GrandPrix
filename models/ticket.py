import pickle
import os

class Ticket:
    def __init__(self, ticket_id, ticket_type, price, validity, features):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price
        self.validity = validity
        self.features = features

def load_tickets():
    if os.path.exists("data/tickets.pkl"):
        with open("data/tickets.pkl", "rb") as f:
            return pickle.load(f)
    return []

def save_tickets(tickets):
    with open("data/tickets.pkl", "wb") as f:
        pickle.dump(tickets, f)
