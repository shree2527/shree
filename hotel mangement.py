import datetime


# Define the Room class
class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def release_room(self):
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} ({self.room_type}) - ${self.price} - Status: {status}"


# Define the Hotel class
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number, room_type, price):
        new_room = Room(room_number, room_type, price)
        self.rooms.append(new_room)

    def show_rooms(self):
        print(f"\n{'-' * 40}\n{'Room Number':<15}{'Room Type':<15}{'Price':<10}{'Status':<10}")
        print('-' * 40)
        for room in self.rooms:
            print(
                f"{room.room_number:<15}{room.room_type:<15}${room.price:<10}{'Booked' if room.is_booked else 'Available'}")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.book_room():
                    print(f"Room {room_number} has been successfully booked!")
                    return True
                else:
                    print(f"Room {room_number} is already booked.")
                    return False
        print(f"Room {room_number} not found.")
        return False

    def check_availability(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        return available_rooms


# Main program
def main():
    hotel = Hotel("Grand Hotel")
    hotel.add_room(101, "Single", 110)
    hotel.add_room(102, "Double", 123)
    hotel.add_room(103, "Suite", 500)

    while True:
        print("\nWelcome to the Hotel Management System")
        print("1. Show available rooms")
        print("2. Book a room")
        print("3. Check room availability")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.show_rooms()
        elif choice == "2":
            room_number = int(input("Enter room number to book: "))
            hotel.book_room(room_number)
        elif choice == "3":
            available_rooms = hotel.check_availability()
            if available_rooms:
                print("Available rooms:")
                for room in available_rooms:
                    print(room)
            else:
                print("No rooms available.")
        elif choice == "4":
            print("Exiting... Thank you for using the Hotel Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the main program
if __name__ == "__main__":
    main()
