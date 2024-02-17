"""
This is a simple project duration estimation calculator, designed with just up to two complexity and environmental factors, solely to demonstrate the technique of use-case points estimation.
The calculator includes the following steps:
    1. Unadjusted Use-Case Weight (UUCW)
    2. Unadjusted Actor Weight (UAW)	
    3. Unadjusted Use-Case Points (UUCP) = UUCW + UAW
    4. Total Technical Factor (TCF)	
    5. Total Environment Factor (EF)	
    6. Adjusted Use-Case Points (UCP) (UCP = UUCP × TCF × EF)
Source: https://www.tutorialspoint.com/estimation_techniques/estimation_techniques_use_case_points.htm
"""

class UseCase():
    
    SimpleUseCaseWeight, SimpleActorWeight = 5, 1
    AverageUseCaseWeight, AverageActorWeight = 10, 2
    ComplexUseCaseWeight, ComplexActorWeight = 15, 3
    UseCases, ActorCases = {'Simple': 0,
                            'Average': 0,
                            'Complex': 0}, {'Simple': 0,
                            'Average': 0,
                            'Complex': 0}

    def __init__(self, NoOfTransactions) -> None:        
        self.NoOfTransactions = NoOfTransactions
        pass        

    def process(self) -> None:
        if NoOfTransactions <= 3:
            self.UseCases["Simple"] = self.UseCases["Simple"] + 1
        elif NoOfTransactions >= 4 and NoOfTransactions <= 7:
            self.UseCases["Average"] = self.UseCases["Average"] + 1
        else :
            self.UseCases["Complex"] = self.UseCases["Complex"] + 1
    
    def calculateUnjustedUCW(self) -> int:
        UUCW = self.SimpleUseCaseWeight * self.UseCases["Simple"] + self.AverageUseCaseWeight * self.UseCases["Average"] + self.ComplexUseCaseWeight * self.UseCases["Complex"]
        return UUCW


class Actor(UseCase):
    
    def __init__(self) -> None:
        pass
    
    def add(self, complexity) -> None:
        if  complexity == 1:
            self.ActorCases["Simple"] = self.ActorCases["Simple"] + 1
        elif  complexity == 2:
            self.ActorCases["Average"] = self.ActorCases["Average"] + 1
        else:
            self.ActorCases["Complex"] = self.ActorCases["Complex"] + 1

    def calculateUnjustedUAW(self) -> int:
        UAW = self.SimpleActorWeight * self.ActorCases["Simple"] + self.AverageActorWeight * self.ActorCases["Average"] + self.ComplexActorWeight * self.ActorCases["Complex"]
        return UAW

class TechnicalComplexity():

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def calculate(t1, t2):
        WeightT1 = 2
        WeightT2 = 1
        return WeightT1 * t1 + WeightT2 * t2

class EnvironmentalComplexity():

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def calculate(t1, t2):
        WeightT1 = -1
        WeightT2 = 1
        return WeightT1 * t1 + WeightT2 * t2


if __name__=="__main__":
    TCF = 0 #complexity factor
    EF = 0 #environmental factor

    while True:
        control = int(input("Press 1 to enter use case, 2 to enter an Actor, 3 to enter technical complexity, 4 to enter environmental complexity or 0 to exit: "))
        
        if control ==  1:

            NoOfTransactions = int(input("Enter a number of transactions"))
            UseCase_ = UseCase(NoOfTransactions)
            UseCase_.process()            

        elif control == 2:

            complexity = int(input("Enter a number of complexity: 1, 2 or 3, where 3 is most complex and 1 the least."))
            Actor_ = Actor()
            Actor_.add(complexity)

        elif control == 3:            

            print(f"Enter a rate from 0 (irrelevant) to 5 (very important) for the following complexity factor: \n T1 - Easy to use: ")
            easy_to_use = int(input())
            print(f"Enter a rate from 0 (irrelevant) to 5 (very important) for the following complexity factor: \n T2 - Portable: ")
            portability = int(input())
            #TechnicalComplexityFactor
            TCF = 0.6 + (TechnicalComplexity().calculate(easy_to_use, portability) * 0.01)

        elif control == 4:
            
            print(f"Enter a rate from 0 (irrelevant) to 5 (very important) for the following environmental factor: \n F1 - Difficult programming language: ")
            easy_to_use = int(input())
            print(f"Enter a rate from 0 (irrelevant) to 5 (very important) for the following environmental factor: \n F2 - Motivation: ")
            portability = int(input())
            #EnvironmentalComplexityFactor
            EF = 1.4 + (-0.03 * EnvironmentalComplexity().calculate(easy_to_use, portability))
            
        else:
            break
    try:
        useCase = UseCase_.calculateUnjustedUCW()
    except:
        useCase = 0
    try:
        actor = Actor_.calculateUnjustedUAW()
    except:
        actor = 0    

    UUCP = useCase + actor
    
    print(f"UUCW is: {useCase} \n UAW is: {actor} \n Unadjusted Use-Case Points: {UUCP}")
    print(f"Adjusted Use-Case Points = {UUCP * TCF * EF}")

        






