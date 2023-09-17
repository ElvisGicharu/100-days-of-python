# We are doing a functions code lab

# We'll be having 3 function examples

# In order for the function to work, we need a driver code and a calling function

# syntax

# def():
    # statements
    
    
# function call
######

# Case study 1
    # printing function
    
# def defineOutput():
#     print('This is my first function')
    
# # defineOutput()
# v=defineOutput()
# print(v)


# case study 2
    # function that calculates area of a Triangle
    
# 

# base= 25
# height= 16

# Function begins here

# def areaTriangle():
#     area= base * height * 0.5
#     print(area)
    
# areaTriangle()


# A function that prints 3 statements

statementA='My brain is tired'
statementB='Take Coffee'
statementC='Go to sleep'
statementD="The weekend was long"

# function starts here

# def statements():
#     a= statementA+statementB
#     b=statementB + statementC
#     c=statementA + statementC
    # print(a)
    # print(b)
    # print(c)

# statements()



        # budget tracker
        
    # inputs
# expenses
# income
# goals

    # logic
    
#unemployed....30,30,30,10
#employed.... 50,30,20
# zero based

    # output
    
# decision
#  goal



#first List  will be income variables
salary= int(input("Enter your income: "))
sideHustle=int(input("Enter your income: "))

# Expenses
utilityBills=int(input("Enter your utility expense: "))
grocery= int(input("Enter your grocery expense: "))
allowances= int(input("Enter your allowances: "))

# Goals
goal1='Improve my setup'
goal2='Go on a Vacation'
goal3='Start a business'
goal4='Education bills'

mygoal=goal1

# if elif will be used for logic

if (mygoal == goal1):
    newincome=salary + sideHustle
    if( newincome >= 40000):
        expense_net= newincome *50/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        
    elif(newincome >= 50000):
        expense_net= newincome *30/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 30/100
        leisure_net= newincome * 10/100
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)
        
    else:
        print('Sorry, your income category isn\'t listed')
        
elif(mygoal == goal2):
    newincome=salary + sideHustle
    if( newincome >= 40000):
        expense_net= newincome *50/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        
    elif(newincome >= 50000):
        expense_net= newincome *30/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 30/100
        leisure_net= newincome * 10/100
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)
        
    else:
        print('Sorry, your income category isn\'t listed')
        
elif(mygoal==goal3):
    newincome=salary + sideHustle
    if( newincome >= 40000):
        expense_net= newincome *50/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        
    elif(newincome >= 50000):
        expense_net= newincome *30/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 30/100
        leisure_net= newincome * 10/100
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)
        
    else:
        print('Sorry, your income category isn\'t listed')
        
else:
    newincome=salary + sideHustle
    if( newincome >= 40000):
        expense_net= newincome *50/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 20/100
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        
    elif(newincome >= 50000):
        expense_net= newincome *30/100
        allowance_net= newincome * 30/100
        savings_net= newincome * 30/100
        leisure_net= newincome * 10/100
        
        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)
        
    else:
        print('Sorry, your income category isn\'t listed')
        
print('My Goal is',goal1)

    
    
        
    











