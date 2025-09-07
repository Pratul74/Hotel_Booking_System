from datetime import datetime
class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number=room_number
        self.room_type=room_type
        self.price_per_night=price_per_night
        self.is_available=True

    def book_room(self):
        if self.is_available:
            self.is_available=False
            return True
        return False
    

    def checkout_room(self):
        self.is_available=True

    def __str__(self):
        return f"Room Number: {self.room_number}, Room Type: {self.room_type}, Price per night: {self.price_per_night}"

class Guest:
    def __init__(self, name, phone_number):
        self.name=name
        self.phone_number=phone_number

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"
    

class Booking:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest=guest
        self.room=room
        self.check_in_date=datetime.strptime(check_in_date,"%Y-%m-%d")
        self.check_out_date=datetime.strptime(check_out_date,"%Y-%m-%d")
        self.total_price=self.calculate_price()

    def calculate_price(self):
        days=(self.check_out_date-self.check_in_date).days
        return days*self.room.price_per_night
    

    def __str__(self):
        return (f"Booking for {self.guest.name} in Room {self.room.room_number},"
                f"from {self.check_in_date.date()} to {self.check_out_date.date()},"
                f"Total: {self.total_price}")
    
class Hotel:
    def __init__(self, name):
        self.name=name
        self.rooms=[]
        self.bookings=[]

    def add_room(self, room):
        self.rooms.append(room)

    def find_available(self):
        return [room for room in self.rooms if room.is_available]
    

    def make_booking(self, guest, room_number, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number==room_number and room.is_available:
                if room.book_room():
                    booking=Booking(guest, room, check_in_date, check_out_date)
                    self.bookings.append(booking)
                    return booking
        return None
    
    def checkout(self, room_number):
        for room in self.rooms:
            if room.room_number==room_number and not room.is_available:
                room.checkout_room()
                return True
        return False
    
                    



    

    


