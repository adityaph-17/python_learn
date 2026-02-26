# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train():

    def __init__(self, name, total_seats, fare, fro, to):
        self.name = name 
        self.total_seats = total_seats
        self.fare = fare
        self.fro = fro
        self.to = to

    def book(self):
        if self.total_seats > 0:
            self.total_seats -= 1
            print(f"Ticket booked successfully! From {self.fro} - To {self.to}")
        else:
            print("Sorry! No seats available.")

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.total_seats}")

    def fare_info(self):
        print(f"Train Name: {self.name}")
        print(f"Fare per ticket: ₹{self.fare}")


# Correct object creation
t = Train("Rajdhani Express", 10, 599, "Mumbai", "Delhi")

t.get_status()
t.book()
t.get_status()
t.fare_info()



        
        