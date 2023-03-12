'''
    Bank:
    -create client (name ,age)
    - withdrow
    -deposite
    -show details
    - show balance
'''
class Bank:
    def __int__(self,name,age):
        print(f'welcome{name}')
        self.name =name
        self.age =age
        self.balance = 0

        def witdrow(self,amount):
            self.balance += amount
            print(f'your current balance :{self.balance}')

        def deposite(self,amount):
            self. balance += amount
            print(f'your current balance: {self.balance}')

            def show_details(self):
                print(f'Name : {self,name}')
                print(f'Age : {self,age}')



