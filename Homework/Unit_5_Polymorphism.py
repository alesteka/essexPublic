from abc import ABC, abstractmethod

"""
Example of polymorphism used over Driverless car.
"""

class abstr(ABC):

    @abstractmethod
    def process(self):
        pass
   
class leftSensor(abstr):
    def __init__(self, left = []):
        self.left = left
                  
    def process(self):       
        for i in self.left:
            print(f"Left sensor has detected {i}")

class rightSensor(abstr):
    def __init__(self, right = []):
        self.right = right

    def process(self):
        for i in self.right:
            print(f"Right sensor has detected {i}")
    

left_sensor = leftSensor(["Cyclist"])  
right_sensor = rightSensor(["Road sign", "Pedestrian"])  

for sensor in (left_sensor, right_sensor):
    sensor.process()