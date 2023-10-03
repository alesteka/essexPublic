import sys
import re
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

#gets the IP number to start a server
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
host = IPAddr
port = 9999

class Report():
    
    data = {} #Dictionary to store reports passed as an imput from a general public 
    employeeData = {} #Dictionary to store the reports and credentials for "ordinary" employee.
    sysData = {} #Dictionary for storing system data e.g Number of logins, timestamp of last login in epoch time.
   
    def __init__(self):
        self.chooseOperation = str(input("1 - Login as employee \n2 - report as a general user\n99 - cancel operation (starts server): "))
        self.sysNumberOfLogs = 0
           
    def choose(self):     
       
        while self.chooseOperation != '1' and self.chooseOperation != "2" and self.chooseOperation != "99":
            chooseOperation = input("1 - Login as employee \n2 - Login as general user\n 99 - cancel operation (starts server): ")
            self.chooseOperation = chooseOperation
                       
            if self.chooseOperation == "1" or self.chooseOperation == "2":
                break
            else:
                continue       

        return self.chooseOperation
  
    def employee(self):
        count = 0
        loginAs = str(input("1 - login as user\n2 - Login as admin "))
        
        while loginAs != "1" and loginAs != "2":
            loginAs = str(input("1 - login as a user\n2 - Login as an admin "))
        

        #Login as a user
        if loginAs == "1":
            if len(self.employeeData) == 0:
                print("There isn't any user yet. Please create one first")
                return
            else:
                name = input("Name: ") 
                password = input("Password: ") 
                print(self.employeeData)
                 
                if name in self.employeeData.keys():
                    if password in self.employeeData[name].keys():
                        print("You have logged in as " + name)
                        self.sysNumberOfLogs += 1
                        timeStart = time.time()
                        
                        while True:                         
                            operation = str(input("Would you like to\n1 - create a report\n2 - update a report\n3 - delete a report\n4 - Go back to login page "))
                            while operation != "1" and operation != "2" and operation != "3" and operation != "4":
                                operation = str(input("Would you like to\n1 - create another report\n2 - update another report\n3 - delete another report\n4 - Go back to login page "))

                            if operation == "1":                                                
                                description = input("Describe the flaw you have encontered: ")

                                if len(self.employeeData[name][password]) == 0:
                                    self.employeeData[name][password][1] = description 
                                
                                else:
                                    val = max(self.employeeData[name][password]) + 1                                   
                                    self.employeeData[name][password][val] = description
                                continue
                            
                            elif operation == "2":                                
                                count += 1

                                while True:
                                    if len(self.employeeData[name][password]) == 0:
                                        print("There is no report. Create one first")
                                        break
                                    try:                                        
                                        print(self.employeeData[name][password])
                                        modify = int(input("Enter the number of a report you wish to update: "))    
                                    except:                                      
                                        continue

                                    if modify in self.employeeData[name][password]:
                                        desc = input("New description: ")
                                        self.employeeData[name][password][modify] = desc
                                        print("successfully updated")
                                        print(self.employeeData)
                                        break
                                    else:
                                        print("There isn't any report with the number " + str(modify))
                                        continue

                            elif operation == "3":
                                count += 1
                                
                                while True:
                                    if len(self.employeeData[name][password]) == 0:
                                        print("There is no report available to delete")
                                        return
                                    try:
                                        delete = int(input("Enter the number of a report you wish to delete: "))
                                        if delete in self.employeeData[name][password]:
                                            print("innnnn")
                                            break                                       
                                        else:
                                            continue
                                    except:
                                        pass
                                
                                for i in self.employeeData[name][password]:
                                    if i == delete:
                                        self.employeeData[name][password].pop(i)
                                        print(f"Report number {i} successfully deleted")                                        
                                        break
                                    else:
                                        continue
                            
                            elif operation == "4":
                                if name in self.sysData.keys():
                                   self.sysData[name]["lastLogin"] = timeStart
                                   self.sysData[name]["numberOfLogins"] = self.sysData[name]["numberOfLogins"] + self.sysNumberOfLogs
                                else:
                                   self.sysData[name] = {}
                                   self.sysData[name]["lastLogin"] = timeStart
                                   self.sysData[name]["numberOfLogins"] = self.sysNumberOfLogs
                                return
                            else:
                                continue
                    else:
                        print(f"Password for a user {name} does not exist.")
                        return
                else:
                    print(f"Name: {name} does not exist.")
                    return        
        
        #Login as admin
        elif loginAs == "2":
            pass_ = input("Enter admin's password (admin): ") 
            if pass_ == "admin":
                print("You have logged in as admin. ")
                while True:                        
                    operation = str(input("Would you like to\n1 - view the reports\n2 - create a user\n3 - view system/event logs\n4 - Logout "))
                    while operation != "1" and operation != "2" and operation != "3" and operation != "4" :
                        operation = str(input("Would you like to\n1 - view the reports\n2 - create a user\n3 - view system/event logs\n4 - Logout "))
                    if operation == "1":
                        print(self.data)
                        print(self.employeeData)
                        continue
                    if operation == "2":
                        name_ = input("Enter user name: ")
                        password_ = input("Enter user password: ")
                        self.employeeData[name_] = {}
                        self.employeeData[name_][password_] = {}
                        print(self.employeeData)
                        continue
                    if operation == "3":
                        print(self.sysData)
                        continue
                    if operation == "4":
                        return
            else:
                print("wrong password")
                return  
        pass

    def general_public(self, report):    

        print("Before reporting the flaw, we would like you to enter the following information, which is required for any additional inquiry.")
        generalName = input("Enter your name: ")     
       
        while not re.match("[a-zA-Z]{2,}", generalName):          
            generalName = input("Invalid name, enter again: ")            
             
        generalEmail = input("Enter your email account:")
        while not re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", generalEmail):          
            generalEmail = input("invalid email account, enter again: ")
        
        generalPhone = input("Enter your phone number:")
        while not re.match(r"^[\+][0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{3,6}$", generalPhone):          
            generalPhone = input("invalid Phone number. Valid phone number example: +919 367 78833")

        description = input("Describe the flaw you have identified")                 
        personalData = {"personalData": [generalName, generalEmail, generalPhone], "flaw": [description]}
        self.data[report] = personalData
        
        print(self.data)
        return           

def main():
    report = 1

    while True:  
        obj = Report()     
        obj.choose()
        if obj.chooseOperation == "1":
            obj.employee()
            pass

        elif obj.chooseOperation == "2":
            obj.general_public(report)
            report += 1             
            pass

        elif obj.chooseOperation == "99":
            break
            #sys.exit("Program has been terminated")

        else:
            break

    server = HTTPServer((host,port), NeuralHTTP)
    server.serve_forever()
    time.sleep(1000)
    server.server_close()

class NeuralHTTP(BaseHTTPRequestHandler, Report):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()        
        #self.wfile.write(bytes(f"<html><body>{self.sysData}</body> </html>", "utf-8"))
        self.wfile.write(bytes(f"<html><body>{self.data}</body> </html>", "utf-8"))

if __name__ == "__main__":
    main()
    