# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class Train:

    def __init__(adi, name, seats):
        adi.name = name
        adi.seats = seats

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.seats}")


t = Train("Rajdhani Express", 10)
t.get_status()




# You can change self to any name.
# self is not a keyword in Python.
# It is just a convention (naming practice).
# Python only requires:
# The first parameter must refer to the object itself.
# But the name can be anything.