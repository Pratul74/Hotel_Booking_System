import datetime as dt
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
        self.check_in_date=check_in_date
        self.check_out_date=check_out_date

    def 
    


