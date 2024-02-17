class methods:
    def __init__(self) -> None:
        pass
    def add(self, x, y): 
        return x + y 
    def subtract(self, x, y): 
        return x - y 
    def multiply(self, x, y): 
        return x * y 
    def divide(self, x, y): 
        return x / y 

class start(methods):
    def __init__(self) -> None:
        self.main = methods() 
    
    def begin(self):
        print("Select operation.") 
        print("1.Add") 
        print("2.Subtract") 
        print("3.Multiply") 
        print("4.Divide") 

        while True: 
            choice = input("Enter choice(1/2/3/4): ")  
            if choice in ('1', '2', '3', '4'): 
                num1 = float(input("Enter first number: ")) 
                num2 = float(input("Enter second number: ")) 
                if choice == '1':
                    print(num1, "+", num2, "=", self.main.add(num1, num2)) 
                elif choice == '2':
                    print(num1, "-", num2, "=", self.subtract(num1, num2)) 
                elif choice == '3':
                    print(num1, "*", num2, "=", self.multiply(num1, num2)) 
                elif choice == '4': 
                    print(num1, "/", num2, "=", self.divide(num1, num2)) 
                    
                next_calculation = input("Let's do next calculation? (yes/no): ") 
                if next_calculation == "no": 
                    break 
            else: print("Invalid Input")

if __name__ == '__main__':
    start1 = start()
    start1.begin()