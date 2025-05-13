import pickle
import os

class PurchaseOrder:
    def __init__(self, order_id, customer_username, tickets, total_price):
        self.order_id = order_id
        self.customer_username = customer_username
        self.tickets = tickets
        self.total_price = total_price

def load_orders():
    if os.path.exists("data/orders.pkl"):
        with open("data/orders.pkl", "rb") as f:
            return pickle.load(f)
    return []

def save_orders(orders):
    with open("data/orders.pkl", "wb") as f:
        pickle.dump(orders, f)
