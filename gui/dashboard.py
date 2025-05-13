import tkinter as tk
from tkinter import messagebox
from models.ticket import load_tickets
from models.order import save_orders, load_orders, PurchaseOrder
import uuid

def show_dashboard(customer):
    window = tk.Tk()
    window.title("Customer Dashboard")
    window.geometry("400x300")
    window.resizable(False, False)

    tk.Label(window, text=f"Welcome, {customer.username}", font=("Arial", 14, "bold")).pack(pady=10)

    def view_and_purchase():
        tickets = load_tickets()
        if not tickets:
            messagebox.showwarning("No Tickets", "No tickets available. Please initialize tickets first.")
            return

        purchase_window = tk.Toplevel(window)
        purchase_window.title("Buy Tickets")
        purchase_window.geometry("350x250")
        purchase_window.resizable(False, False)

        selected = tk.StringVar(purchase_window)
        selected.set(tickets[0].ticket_type)

        tk.Label(purchase_window, text="Select Ticket:", font=("Arial", 10)).pack(pady=10)
        tk.OptionMenu(purchase_window, selected, *[t.ticket_type for t in tickets]).pack(pady=5)

        def purchase(ticket_type):
            for t in tickets:
                if t.ticket_type == ticket_type:
                    order_id = str(uuid.uuid4())
                    order = PurchaseOrder(order_id, customer.username, [t], t.price)
                    all_orders = load_orders()
                    all_orders.append(order)
                    save_orders(all_orders)
                    customer.orders.append(order)

                    messagebox.showinfo(
                        "Purchase Successful",
                        f"✅ Ticket: {t.ticket_type}\n💵 Price: ${t.price}\n🧾 Order ID: {order_id}"
                    )
                    break

        tk.Button(purchase_window, text="Confirm Purchase", width=20,
                  command=lambda: purchase(selected.get())).pack(pady=20)

    def show_orders():
        if not customer.orders:
            messagebox.showinfo("My Orders", "No purchases yet.")
            return

        order_window = tk.Toplevel(window)
        order_window.title("My Orders")
        order_window.geometry("400x300")
        order_window.resizable(False, False)

        tk.Label(order_window, text="My Purchase Orders", font=("Arial", 12, "bold")).pack(pady=10)

        for order in customer.orders:
            ticket_names = ", ".join([t.ticket_type for t in order.tickets])
            summary = (
                f"Order ID: {order.order_id}\n"
                f"Tickets: {ticket_names}\n"
                f"Total: ${order.total_price}\n"
                "--------------------------"
            )
            tk.Label(order_window, text=summary, justify="left", anchor="w").pack(padx=10, pady=5)

    # Buttons
    tk.Button(window, text="🎫 Buy Tickets", width=20, height=2, command=view_and_purchase).pack(pady=10)
    tk.Button(window, text="📋 My Orders", width=20, height=2, command=show_orders).pack(pady=10)

    window.mainloop()

def show_admin_dashboard():
    window = tk.Tk()
    window.title("Admin Dashboard")
    window.geometry("400x300")
    window.resizable(False, False)

    orders = load_orders()
    sales_summary = {}

    for order in orders:
        sales_summary[order.customer_username] = sales_summary.get(order.customer_username, 0) + len(order.tickets)

    tk.Label(window, text="🎯 Ticket Sales Summary", font=("Arial", 14, "bold")).pack(pady=10)

    if not sales_summary:
        tk.Label(window, text="No ticket sales yet.").pack(pady=10)
    else:
        for user, count in sales_summary.items():
            tk.Label(window, text=f"{user}: {count} ticket(s)").pack(pady=5)

    window.mainloop()
