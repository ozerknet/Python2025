class Person:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        
    def updateContact(self):
        print(self.name, self.phone, self.address, self.email)  
        

class Customer(Person):
    def __init__(self, name, phone, address, email, CustomerID):
        super().__init__(name, phone, address, email)
        self.customerID = CustomerID
    def purchase(self):
        pass
    

class Employee(Person):
    def __init__(self, name, phone, address, email, EmployeeID):
        super().__init__(name, phone, address, email)
        self.EmployeeID = EmployeeID
    def promote(self):
        pass
    def retire(self):
        pass
    
    

class Courier(Person):
    def __init__(self, name, phone, address, email):
        super().__init__(name, phone, address, email)
    def deliverPackage(self):
        pass
    
    
abc = input("Enter name, phone, address, email")
print("Details: " + abc)