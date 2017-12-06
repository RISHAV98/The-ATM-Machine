def account():
    print ("Welcome to the bokuwabank ATM terminal v1.0")
        print ("Please enter your pin number")
        account = raw_input("Pin number is 1337: ")
        account = (1337)

account()

def balance():
    print "View your balance?"
    see = raw_input("Enter Y or N: ")
    if (see == "y") or (see == "Y"):
        balance = int(0)
    print ("Current balance: $" + str(balance))

balance()

def edit():
    print "Would you like to deposit/withdraw?"
    print "D == Deposit"
    print "W == Withdraw"
    print "Q == Quit"
    print "Please note input is case-sensitive"
    see = raw_input("Enter D, W or Q.")

    if (see == "D"):
        def deposit():
            print "How much would you like to deposit into your account?"
            deposit = input("Enter amount to deposit: ")
            deposit = int(deposit)

            currentbalance = deposit + balance
            print ("Deposited: $" + str(deposit))
            print ("Current Balance: $" + str(currentbalance))

    deposit()

    if (see == "W"):
        def withdraw():    
                print "How much would you like to withdraw from your account?"
            withdraw = input("Enter amount to withdraw: ")
            withdraw = int(withdraw)

            currentbalance = withdraw - balance
            print ("Withdrew: $" + str(withdraw))
            print ("Current Balance: $" + str(currentbalance))

    withdraw()        

    else:
        print "Invalid input."
        edit()

edit()



def withdraw():    
    if (answer == "W") or (answer == "w"):
        print ("How much would you like to withdraw from your account?")
        withdraw = input("Enter amount to withdraw: ")
        withdraw = int(withdraw)

        currentbalance = withdraw - balance
        print ("Withdrew: $" + str(withdraw))
        print ("Current Balance: $" + str(currentbalance))

withdraw()        

def quit():
    if (answer == "Q"):
        exit ("Thank you for doing business with bokuwabank")

    else:
        exit ("Thank you for doing business with bokuwabank")

quit()
