import random


# Define the Taxi class
class Taxi:
    def __init__(self, taxi_id, model, rate_per_km):
        self.taxi_id = taxi_id
        self.model = model
        self.rate_per_km = rate_per_km
        self.is_available = True

    def book_taxi(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def release_taxi(self):
        self.is_available = True

    def calculate_fare(self, distance):
        return self.rate_per_km * distance

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Taxi {self.taxi_id} ({self.model}) - Rate: ${self.rate_per_km}/km - Status: {status}"


# Define the TaxiService class
class TaxiService:
    def __init__(self, name):
        self.name = name
        self.taxis = []

    def add_taxi(self, taxi_id, model, rate_per_km):
        new_taxi = Taxi(taxi_id, model, rate_per_km)
        self.taxis.append(new_taxi)

    def show_taxis(self):
        print(f"\n{'-' * 40}\n{'Taxi ID':<15}{'Model':<15}{'Rate':<10}{'Status':<10}")
        print('-' * 40)
        for taxi in self.taxis:
            print(
                f"{taxi.taxi_id:<15}{taxi.model:<15}${taxi.rate_per_km:<10}{'Available' if taxi.is_available else 'Booked'}")

    def book_taxi(self, taxi_id):
        for taxi in self.taxis:
            if taxi.taxi_id == taxi_id:
                if taxi.book_taxi():
                    print(f"Taxi {taxi_id} has been successfully booked!")
                    return taxi
                else:
                    print(f"Taxi {taxi_id} is already booked.")
                    return None
        print(f"Taxi {taxi_id} not found.")
        return None

    def check_availability(self):
        available_taxis = [taxi for taxi in self.taxis if taxi.is_available]
        return available_taxis


# Main program
def main():
    taxi_service = TaxiService("Quick Ride Taxi Service")
    taxi_service.add_taxi(101, "Toyota Prius", 1.5)
    taxi_service.add_taxi(102, "Honda Civic", 1.8)
    taxi_service.add_taxi(103, "Ford Explorer", 2.0)

    while True:
        print("\nWelcome to the Taxi Booking System")
        print("1. Show available taxis")
        print("2. Book a taxi")
        print("3. Calculate fare")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            taxi_service.show_taxis()
        elif choice == "2":
            taxi_id = int(input("Enter the taxi ID to book: "))
            booked_taxi = taxi_service.book_taxi(taxi_id)
            if booked_taxi:
                distance = float(input("Enter the distance (in km): "))
                fare = booked_taxi.calculate_fare(distance)
                print(f"Your fare for {distance} km is: ${fare:.2f}")
                print("Thank you for booking!")
        elif choice == "3":
            taxi_id = int(input("Enter the taxi ID to calculate fare: "))
            taxi = next((taxi for taxi in taxi_service.taxis if taxi.taxi_id == taxi_id), None)
            if taxi:
                distance = float(input("Enter the distance (in km): "))
                fare = taxi.calculate_fare(distance)
                print(f"The fare for {distance} km is: ${fare:.2f}")
            else:
                print("Taxi not found!")
        elif choice == "4":
            print("Exiting... Thank you for using the Taxi Booking System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the main program
if __name__ == "__main__":
    main()
