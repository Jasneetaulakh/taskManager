# this programme will allow the user to access an investment calculator or home loan repayment calculator

# it will begin by asking the user which calculator they want to access

# if neither option is entered, an error message will appear

# if investment is entered, further questions will be asked to finally calculate the  total  investment.

# if bond is entered, different questions will be asked to calculate the total loan to be repayed.

import math

print("This programme is an investment or bond calculator. \nInvestment: amount of interest you will earn on your interest \nBond: the amount you will have to pay on a home loan.")

finance_calculator = input("Enter which calculator you would like to use today, Investment or Bond: ")
user_calculator = finance_calculator.lower()    #convert user input to all lower case 

if user_calculator == "investment" or user_calculator == "bond":    
    print(f"You have chosen the {user_calculator} calculator. Lets begin. ")
else:
    print("You have entered an invalid option. ")


if user_calculator == "investment":     # if user entered investment, the following answers are required for the calculation 
    deposit_money = float(input("Enter how much money you are depositing? "))
    user_interest_rate = input("Enter the interest rate as a percentage: ")
    interest_rate = float(user_interest_rate.strip("%")) / 100    # in case user entered the % sign, remove from user input and divide by 100
    time = float(input("How many years are you planning to invest for? "))
    interest = input("Would you like to go for simple or compound interest?: ")

    if interest == "simple":        #use if statment here depending if user entered simple or compound 
        total = deposit_money * (1 + (interest_rate / 100) * time)
    elif interest == "compound":
        total = deposit_money * math.pow((1 + (interest_rate /100)), time)

    total_amount = round(total, 2)  # total amound rounded to 2 decimal places, thats usually how money is written 

    print(f"Based on the information above, your investment will be £{total_amount} ")
    
if user_calculator == "bond":       # if user entered bond, different answers are required 
    house_value = float(input("Enter the present value of your house: "))
    user_interest_rate = input("Enter the interest rate as a percentage: ")
    interest_rate_y = float(user_interest_rate.strip("%")) / 100
    time_months = float(input("Enter the number of months you will take to repay the bond: "))
    interest_rate_m = interest_rate_y / 12
    total = (house_value * interest_rate_m) / (1 - (math.pow((1 + interest_rate_m), (-time_months))))
    total_amount = round(total, 2)
    
    print(f"Based on the information above, the total amount you will have to repay each month is £{total_amount} ")
