import random
import tkinter as tk
#why didnt this work
class BusBookingApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Bus Booking App")
        self.geometry("300x300")
        self.resizable(False, False)
        
        self.password1 = "batlor"  # the password is initialized assuming those were the registered ones
        self.user_name1 = "charles"  # the username is initialized assuming those were the registered ones
        self.user_name = ""
        self.password = ""
        self.choice = 0
        self.n = 0
        self.cost = 0
        
        self.login_frame()
    
    def login_frame(self):
        self.clear_frame()
        
        login_label = tk.Label(self, text="Enter login details")
        login_label.pack(pady=10)
        
        user_name_label = tk.Label(self, text="Username")
        user_name_label.pack()
        
        self.user_name_entry = tk.Entry(self)
        self.user_name_entry.pack()
        
        password_label = tk.Label(self, text="Password")
        password_label.pack()
        
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)
    
    def menu_frame(self):
        self.clear_frame()
        
        menu_label = tk.Label(self, text="Menu")
        menu_label.pack(pady=10)
        
        booking_status_button = tk.Button(self, text="Booking status", command=self.booking_status)
        booking_status_button.pack()
        
        bus_booking_button = tk.Button(self, text="Bus booking", command=self.bus_booking)
        bus_booking_button.pack()
        
        booking_payment_button = tk.Button(self, text="Booking payment", command=self.booking_payment)
        booking_payment_button.pack()
        
        booking_report_button = tk.Button(self, text="Booking report", command=self.booking_report)
        booking_report_button.pack()
        
        sign_out_button = tk.Button(self, text="Sign out", command=self.sign_out)
        sign_out_button.pack(pady=10)
    
    def booking_status_frame(self):
        self.clear_frame()
        
        booking_status_label = tk.Label(self, text="Booking status")
        booking_status_label.pack(pady=10)
        
        # TODO: implement booking status functionality
        
        back_button = tk.Button(self, text="Back", command=self.menu_frame)
        back_button.pack(pady=10)
    
    def bus_booking_frame(self):
        self.clear_frame()
        
        bus_booking_label = tk.Label(self, text="Bus booking")
        bus_booking_label.pack(pady=10)
        
        seats_label = tk.Label(self, text="Number of seats")
        seats_label.pack()
        
        self.seats_entry = tk.Entry(self)
        self.seats_entry.pack()
        
        bus_type_label = tk.Label(self, text="Bus type")
        bus_type_label.pack()
        
        self.bus_type_var = tk.StringVar(self)
        self.bus_type_var.set("Ordinary")
        bus_type_option = tk.OptionMenu(self, self.bus_type_var, "Ordinary", "Luxury")
        bus_type_option.pack()
        
        book_button = tk.Button(self, text="Book", command=self.book)
        book_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back", command=self.menu_frame)
        back_button.pack()
    
    def booking_payment_frame(self):
        self.clear_frame()
        
        booking_payment_label = tk.Label(self, text="Booking payment")
        #booking_payment_label.pack(pady=
