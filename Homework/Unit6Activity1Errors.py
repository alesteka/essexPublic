
x = input("Enter a number: ")
try:
    x = int(x)
    if x != 5:
       raise ValueError
    result = 10 / x
except:
   
   if x == 0:
      raise ZeroDivisionError
   elif type(x) != type(int()):
      raise TypeError
   elif x != 5:
      raise ValueError
   else:
      print("other error")
   

