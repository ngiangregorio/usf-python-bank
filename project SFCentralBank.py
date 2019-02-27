# Lists of usernames, passwords, and balances.
usernames = []
passwords = []
balances = []

# Current user logged in. Changes with each log in.
# Allows bank() to access current users balance.
currentUser = ()


def SFCentralBank():
    # Starting screen with registration and log in functions.
    global currentUser
    print("\n\n\t******** Main Menu ********\n")
    print("\n\nWelcome to SF Central Bank!\n\nOptions:")
    print("\n\t1.  Register")
    print("\t2.  Log in")
    print("\t3.  Quit")
    while True:
        num = int(input("Make a selection from the options menu: "))
        if num == 1:
            register()
            return SFCentralBank()
        elif num == 2:
            # Log in function.
            username = input("Enter username: ")
            if checkUsername(username):
                password = input("Enter password: ")
                if checkPassword(password):
                    currentUser = username
                    print("\n\n\t******** Welcome, " + currentUser + "! ********")
                    return bank()
                    # Only allows bank() access if username and password are correct.
                else:
                    print("\n\\nt******** Invalid password. ********\n")
            else:
                print("\n\n\t******** Invalid username. ********\n")
                return SFCentralBank()
        elif num == 3:
            print("\n\nHave a nice day.")
            return
        else:
            print("\n\n\t******** Invalid selection. ********\n")
            return
        break


def register():
    # Registration function -- creates username and password
    # and adds them to their lists.
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    username = firstname + lastname
    username = username.lower()
    if username not in usernames:
        usernames.append(username)
        # Adds username to list.
        balances.append(int(1000))
        # Adds $1,000 balance to username's account
        print("\n\n\t******** Success! Account created. ********")
        print("\n\tUsername:", username)
    else:
        print("\n\n\t******** Error. Username already exists. ********\n")
    password = ""
    for i in lastname.lower():
        password = i + password
        # Makes lowercase reversed lastname password.
    if password not in passwords:
        passwords.append(password)
        # Adds password to list
        print("\tPassword:", password)
        return


def checkUsername(x):
    # Checks if username is valid and
    # returns to SFCentralBank main menu if invalid.
    if x in usernames:
        return True
    else:
        return


def checkPassword(y):
    # Checks if password is valid and
    # returns to SFCentralBank main menu if invalid.
    if y in passwords:
        return True
    else:
        return


def bank():
    # Banking options for current logged in user.
    userBalIndex = usernames.index(currentUser)
    # Finds index position of current user in usernames list.
    bal = balances[userBalIndex]
    # Finds current user's balance based on corresponding index.
    print("\n\nBanking options:")
    print("\n\t1.  Make a deposit")
    print("\t2.  Make a withdrawal")
    print("\t3.  Show balance")
    print("\t4.  Log out")
    print("\t5.  Quit")
    while True:
        num = int(input("Make a selection from the options menu: "))
        if num == 1:
            deposit = float(input("Enter amount of deposit: "))
            bal += deposit
            balances[userBalIndex] = bal
            # Updates user's balance in balances list.
            print("\nDeposit processed.\nBalance: ${0:,.2f}".format(bal))
        elif num == 2:
            withdrawal = float(input("Enter amount of withdrawal: "))
            if withdrawal > bal:
                print("\n\n\t******** Denied. ********\n")
                print("\n\tMaximum withdrawal is ${0:,.2f}".format(bal))
            else:
                bal -= withdrawal
                balances[userBalIndex] = bal
                # Updates user's balance in balances list.
                print("\nWithdrawal processed.\nBalance: ${0:,.2f}".format(bal))
        elif num == 3:
            print("\nBalance: ${0:,.2f}".format(bal))
        elif num == 4:
            return SFCentralBank()
        elif num == 5:
            print("\n\nHave a nice day.")
            break
        else:
            print("\n\n\t******** Invalid selection. ********\n")


SFCentralBank()
