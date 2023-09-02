#You are working on a Python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately.

#You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.

#Update the class with the default color for all vehicles," white".

#Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle

#Create a method to display all the properties of an object of the class

#Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.

Class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("maximum Speed", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 50000)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 75000)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()