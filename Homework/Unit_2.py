


class Employee():

    def __init__(self, firstName, lastName, jobTitle, salary, leave = "NA") -> None:
        self._firstName = firstName    
        self.lastName = lastName 
        self.jobTitle = jobTitle
        self.salary = salary
        self.leave = leave

    def append(self):
        list = []       
        list.append(self._firstName)
        list.append(self.lastName)
        list.append(self.jobTitle)
        list.append(self.salary)
        list.append(self.leave)
        return list

    def bookLeave(self, leave):
        self.leave = leave
    
    def newDict(self):
        return self.append()

    def updateDatabase(self, database):        
        count = 0
        newValue = self.newDict()
        for case in database:
            if self._firstName in case:
                database.pop(count)
                database.append(newValue)
                count += 1
                return database
            else:
                pass


database = []
e1 = Employee("Donald", "Smith", "Software Developer", 4000)
e2 = Employee("Jack", "Jones", "Analyst", 3900)

for obj in (e1, e2):
    database.append(obj.append())

e1.bookLeave("From 1st of January until 5th of January")
updated = e1.updateDatabase(database)
print(updated)       
