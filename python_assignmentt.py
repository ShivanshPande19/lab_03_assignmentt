class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price
    
    def display_details(self):
        print(f"Flight ID: {self.flight_id}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Price: {self.price}")
        print()

class FlightDatabase:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_flight_id(self, flight_id):
        found = False
        for flight in self.flights:
            if flight.flight_id == flight_id:
                flight.display_details()
                found = True
                break
        if not found:
            print("Flight not found.")
    
    def search_by_source(self, source):
        found = False
        for flight in self.flights:
            if flight.source == source:
                flight.display_details()
                found = True
        if not found:
            print("No flights found from the given source.")
    
    def search_by_destination(self, destination):
        found = False
        for flight in self.flights:
            if flight.destination == destination:
                flight.display_details()
                found = True
        if not found:
            print("No flights found to the given destination.")

# Creating flight objects
flights = [
    Flight("AI161E90", "BLR", "BOM", 5600),
    Flight("BR161F91", "BOM", "BBI", 6750),
    Flight("AI161F99", "BBI", "BLR", 8210),
    Flight("VS171E20", "JLR", "BBI", 5500),
    Flight("AS171G30", "HYD", "JLR", 4400),
    Flight("AI131F49", "HYD", "BOM", 3499)
]

# Creating flight database
flight_database = FlightDatabase()
for flight in flights:
    flight_database.add_flight(flight)

# Taking user input
user_input = int(input("Enter 1 to search by Flight ID, 2 for source city, 3 for destination city: "))

if user_input == 1:
    flight_id = input("Enter Flight ID: ")
    flight_database.search_by_flight_id(flight_id)
elif user_input == 2:
    source = input("Enter source city: ")
    flight_database.search_by_source(source)
elif user_input == 3:
    destination = input("Enter destination city: ")
    flight_database.search_by_destination(destination)
else:
    print("Invalid input.")
