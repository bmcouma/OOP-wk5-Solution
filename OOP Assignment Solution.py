# Assignment 1: Design Your Own Class - Superhero Theme

class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self._name = name  # Encapsulated attribute
        self._power_level = power_level
        self._secret_identity = secret_identity
        self._is_active = True

    def use_power(self):
        if self._is_active:
            return f"{self._name} unleashes their power at level {self._power_level}!"
        return f"{self._name} is currently retired."

    def reveal_identity(self):
        return f"{self._name}'s secret identity is {self._secret_identity}."

    def retire(self):
        self._is_active = False
        return f"{self._name} has retired from hero work."

    def get_name(self):
        return self._name

# Inheritance: FlyingSuperhero extends Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)
        self._flight_speed = flight_speed

    def use_power(self):
        if self._is_active:
            return f"{self._name} soars through the sky at {self._flight_speed} mph!"
        return f"{self._name} is currently retired."

    def boost_speed(self, increase):
        self._flight_speed += increase
        return f"{self._name}'s flight speed increased to {self._flight_speed} mph!"

# Assignment 2: Polymorphism Challenge - Vehicles

class Vehicle:
    def move(self):
        pass  # Abstract method to be overridden

class Car(Vehicle):
    def move(self):
        return "Driving on the highway 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the clouds ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the waves ⛵"

# Demo code to test the classes
def main():
    print("=== Superhero Demo ===")
    # Create a regular superhero
    hero = Superhero("Captain Thunder", 85, "Alex Smith")
    print(hero.use_power())
    print(hero.reveal_identity())
    print(hero.retire())
    print(hero.use_power())

    # Create a flying superhero
    flying_hero = FlyingSuperhero("Sky Blazer", 90, "Emma Jones", 500)
    print(flying_hero.use_power())
    print(flying_hero.boost_speed(100))
    print(flying_hero.reveal_identity())

    print("\n=== Vehicle Demo ===")
    # Polymorphism with vehicles
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())

if __name__ == "__main__":
    main()