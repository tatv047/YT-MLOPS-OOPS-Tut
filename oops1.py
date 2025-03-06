# intitiate a class
class employee:
    # special function/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("attributes/data has been initiated")

    # create methods
    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Emloyee is now travelling to {destination}")

    
# create an object/instance of the Class
sam = employee()
sam.travel("Agra")
# print(sam)
