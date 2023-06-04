#User bank app
#Create User Class

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

        #FORMAT FOR PRINTING USER INFO
    def __repr__(self):
        return self.name + " " + self.pin + " " + self.password

    #CHANGE NAME
    def change_name(self, new_pin, name):
        self.new_pin = new_pin
        if new_pin != self.pin:
            print("Incorrect Pin")
        else:
            self.name = name
            print("Updated Name:", self.name)

    #CHANGE PIN
    def change_pin(self, current_pin, new_pin):
        self.new_pin = new_pin
        if current_pin != self.pin:
            print("Incorrect Pin")
        else:
            self.pin = new_pin
            print("Updated Pin:", self.pin)

    def change_password(self, current_password, new_password):
        self.new_password = new_password
        if current_password != self.password:
            print("Incorrect Password")
        else:
            self.password = new_password
            print("New Password:", self.password)





#BANK ACCOUNT USER
class BankUser(User):
    def __init__ (self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    #SHOW BALANCE
    def show_balance(self, balance):
        self.balance = balance
        print("Updated Balance:", self.balance)
        return balance

    #DEPOSIT FUNDS
    def deposit_funds(self, deposit):
        self.balance += deposit
        print("Deposit Amount:", deposit)
        print("New Balance:", self.balance)

    #WITHDRAW FUNDS
    def withdraw_funds(self, withdraw):
        if self.balance <= withdraw:
            print("Insufficent Funds")
        else:
            self.balance -= withdraw
            print("Withdrawl Amount:", withdraw)
            print("New Balance:", self.balance)
            return self.balance

    #TRANSFER FUNDS
    def transfer_funds(self, access_pin, transfer_name, transfer_amount):
        self.trasfer_amount = transfer_amount
        self.transfer_name = transfer_name
        self.access_pin = access_pin
        if access_pin != self.pin:
            print("Incorrect Pin")
        else:
            if transfer_amount <= 0:
                print("Insufficent Funds")
            elif transfer_amount > self.balance:
                print("Insufficent Funds")
            else:
                self.balance -= transfer_amount
                print("Transfer Amount:", transfer_amount)
                print("Transferred Funds To:", transfer_name)
                print("New Balance:", self.balance)
                return self.balance

    def request_funds(self, receiving_user, request_pin, request_password, request_amount):
        if request_pin != receiving_user:
            print("Incorrect PIN")
            return False
        if request_password != self.password:
            print("Incorrect Password")
            return False

        if request_amount <= 0:
            print("Insufficent Funds")
            return False
        if request_amount > self.balance:
            print("Insufficent Funds")

        self.balance -= request_amount
        receiving_user.balance += request_amount
        print("Transfer of", request_amount, "completed.")
        print("NEw Balance (Requesting User):", self.balance)
        print("New Balance (Receiving User:)", receiving_user.balance)
        return True



user_one = BankUser("jace", "1111", "password")
print(user_one)
print(user_one.change_name("1111", "jack"))
print(user_one)
print(user_one.change_pin("1111", "2121"))
print(user_one)
print(user_one.change_password("pas", "newpassword"))
print(user_one.deposit_funds(10000))
print(user_one.withdraw_funds(5000))
print(user_one.transfer_funds("2121", "Jazz", 2000))
print(user_one.transfer_funds("2121", "Jada", 1000))
#should be insufficent
print(user_one.transfer_funds("2121", "Jace", 1000))
print(user_one.request_funds("Jace", "2121", "newpassword", 44))
