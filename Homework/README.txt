
# Command line prototype of the flaw reporting service application
# Team 1
# 12.06.2023
# ***Program version used: Python 3.11.0***


1. Description of the prototype

The working prototype has been implemented with the OOP approach using Python, which will also be used for the final assignment.
To demonstrate the operations that have been discussed in the design proposal document i.e. CRUD operations, we have primarily used a dictionary as a data structure, together with a list to simulate the database.

In the beginning, the client gets a prompt display, to choose between the options to either report the flaw directly, as a general user, to log in as an employee, or to cancel the operation. The former has some additional checks for example, the user has to provide his name, email and phone number, whereas each has to be filled with a certain pattern. E.g. phone number has to start with the + sign. We have decided to implement this as the regular expression, to demonstrate an additional step of security check, that we should take into account for the final assignment. For demonstrational purposes, the user has to describe the flaw, otherwise, for the final assignment, there should be some additional options to fill in, for example, the type of a flaw, the domain name of the website, how to reproduce the flaw (if possible), etc.

On the other hand, the client can log in as an employee, whereas he gets another prompt, to choose between the admin and user roles. Corresponding to the roles, the client is able to perform its operations. Moreover, to use the 'user' role, the admin has to create one first. Once the user role is created, its actions are monitored, to simulate event log monitoring of the system.

With the use of a library namely requests, we have tried to demonstrate, how the get request of an API call should look like/and be implemented, to communicate with the server and consequently with the database.


2. How to execute the code:

***Password for the admin log in is: 'admin'***

The code can be executed through an IDE's main terminal/shell, whereas the initial input should be as follows (assuming that the Python interpreter is already installed): Python <path to the python executable file>. E.g. Python commandLineApp.py. Any additional parameters are not required, because the program guides the user through entire process.


3. To send the get request through an API call, one has to follow these steps (for a windows user):
	3.0 Start the Application and press 99 to immediately start the server (to display some kind of data, one should first create a report as a general user)
	3.1 Open another terminal and type ipconfig to get the ip of your local computer (under Ethernet adapter - IPv4 Address).
	3.2 Type: "curl <ip Address>:9999" E.g "curl 192.168.1.6:9999".
	3.3 The output should be either empty or filled dictionary.