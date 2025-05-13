import pickle
import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Customer(User):
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email
        self.orders = []

def load_customers():
    if os.path.exists("data/customers.pkl"):
        with open("data/customers.pkl", "rb") as f:
            return pickle.load(f)
    return {}

def save_customers(customers):
    with open("data/customers.pkl", "wb") as f:
        pickle.dump(customers, f)
