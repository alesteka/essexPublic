class Car:
    def __init__(self):
        self.cars = {
            "Ford": {
                "Model": ["Mustang", "Fiesta", "Focus"],
                "Year": [1964, 1976, 1998],
                "Price": [5000, 2000, 4000]
            },
            "Chevrolet": {
                "Model": ["Camaro", "Impala", "Corvette"],
                "Year": [1967, 1980, 2005],
                "Price": [6000, 3000, 8000]
            },
            "BMW": {
                "Model": ["M3", "M5", "X5"],
                "Year": [1995, 2000, 2010],
                "Price": [10000, 12000, 15000]
            }
        }
        
    def items(self):
        return self.cars.items()

    def keys(self):
        return self.cars.keys()

    def values(self):
        return self.cars.values()
    
print(Car().items())
print(Car().keys())
print(Car().values())