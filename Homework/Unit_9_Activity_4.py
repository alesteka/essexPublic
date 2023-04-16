

class assertControl():
    
    # Python String Operations
    str1 = 'Hello'
    str2 ='World!'
    
    def __init__(self) -> None:
        pass

    def equal_strings(self):
        return (assertControl.str1 == assertControl.str2)

    def concatenation(self):
        
        # using +
        #print('str1 + str2 = ', assertControl.str1 + assertControl.str2)
        return(assertControl.str1 + assertControl.str2)  

    def multiply(self):

        # using *
        #print('str1 * 3 =', assertControl.str1 * 3)
        return(assertControl.str1 * 3)