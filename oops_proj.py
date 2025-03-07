"""
Dummy social media project for understanding classes and objects. 
"""

class chatbook:

    __user_id = 1 # static variable and can only be accessed by the class not self.

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User" # a hidden attribute now - encapsulation
        # self.user_id = 0
        # self.user_id+= 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()


    @staticmethod # you don't need self for static method because it's not the object accessing it, hence it's also diff this way 
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value 

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value
    
    def menu(self):
        user_input = input("""Welcome to ChatBook !! How would you like to proceed?
                        1. Press 1 to signup
                        2. Press 2 to signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friend
                        5. Press any other key to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email = input("enter your email here ->")
        pwd = input("setup your password here->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !")
        print("\n") 
        self.menu()
    
    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu!!")
        else:
            uname = input("enter your username here->")
            pwd = input("enter your password here->")
            
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input the correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your message here ->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signup first to post something")

        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here->")
            frnd = input("Whom to send the msg? ->")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to sign in first !!")

        print("\n")
        self.menu()

# obj = chatbook()