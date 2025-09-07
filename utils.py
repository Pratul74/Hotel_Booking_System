class Room:
    def __init__(self, room_number, room_type, price_per_night, is_available):
        self.room_number=room_number
        self.room_type=room_type
        self.price_per_night=price_per_night
        self.is_available=is_available

    def book_room(self):
        pass

    def checkout_room(self):
        pass

    def __str__(self):
        pass

class Guest:
    def __init__(self, name, phone_number):
        self.name=name
        self.phone_number=phone_number

    def __str__(self):
        pass

