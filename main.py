from utils import Room, Guest, Booking, Hotel

if __name__=="__main__":
    hotel=Hotel("Taz Hotel")
    room1=Room(100,"Single",1000)
    room2=Room(105,"Double",3000)
    room3=Room(106,"Double",3000)
    room4=Room(110,"Triple",5000)
    room5=Room(117,"Quad",8000)
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)
    hotel.add_room(room4)
    hotel.add_room(room5)
    guest1=Guest("Pratul Kumar","7004644521")
    guest2=Guest("Rahul Raj","9133427892")
    print("Showing available rooms: ")
    for room in hotel.find_available():
        print(room)
    booking1=hotel.make_booking(guest1,100,"2025-09-12","2025-09-22")
    if booking1:
        print(booking1)
    hotel.checkout(100)
    print("Room Number 100 checked out")
    print("Available Rooms after check out: ")
    for room in hotel.rooms:
        print(room)


