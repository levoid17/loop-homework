# Rocket launch


for i in range (10 , 0 , -1):
    print(i)
print ("liftoff!")


# Cinema tickets


child_tickets=0
adult_tickets=0
for i in range (1,6):
   visitor_age = int(input(f"Enter your age visitor {i}: "))
   if visitor_age  <= 17 and visitor_age>=0:
       child_tickets+=1
   elif visitor_age > 17 and visitor_age>=0 :
       adult_tickets+=1
   else :
       print("invalid age.")
       break
print(f"adult tickets: {adult_tickets}")
print(f"Children tickets: {child_tickets}")


# Read the code answer is 1 3 5 7 9 


#shopping basket


Total_price=0
for i in range (1,6):
    item_price=float(input(f"price of item {i}: "))
    Total_price+=item_price
print(f"Total: {Total_price:.2f}")
print(f"Overall: {(Total_price)/5:.2f}")


#choose a passport


i=1
while 2>i:
    user_passport = input("New passport: ")
    if len(user_passport)>8:
        break
    else:
        print("Too short,try again")
        continue
print("Password accepted")


#Read the code 70 40 10 -20 Done


#Step counter


for i in range(1,8):
    steps_count= 1200*i
    print(f"Day {i}: {steps_count}")


#Simple login


Username='admin'
Password='1234'
for i in range(1,4):
    user_name=input('Enter your username: ')
    password=input('Enter your password: ')
    if user_name==Username and password==Password:
        print('Welcome!')
        break
    else:
        print('Wrong username or password')


#ATM withdrawal


withdrawal_limit=500
i=1
while i<2:
    withdraw_amount=int(input('How much you want to withdraw: '))
    if withdraw_amount==0:
       print('goodbye')
       break
    elif withdraw_amount<0:
        print('invalid amount')
    elif withdraw_amount>withdrawal_limit:
        print('insufficient amount')
    else:
        withdrawal_limit-=withdraw_amount
        print(f'Balance: {withdrawal_limit}')


#read the code PIN: 1111 Wrong PIN, 2 attempts left PIN: 2222 Wrong PIN, 1 attempts left PIN: 1234 Access granted Attempts used: 3


#exam results


k=-1
i=0
b=0
total_grade=0
passed=0
failed=0
while i>-1:
    students_grade=int(input('Grade: '))
    total_grade+=students_grade
    b=b+1
    if k<students_grade:
        k=students_grade
    if students_grade>=51 and students_grade<=100:
        passed+=1
    elif students_grade == -1 :
        break
    else:
        failed+=1
print(f"Highest: {k}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {total_grade/(b-1)}")

#parking garage


free_spaces = 20

while True :
    command = input("write: in/out/stop").lower()
    if command == "in" :
        free_spaces -= 1
    elif command == "out":
        free_spaces += 1
    elif command == "stop":
        break
    else :
        print("Unknown command")
    if free_spaces == 20 and command == "in":
        print("Garage is full")
    elif free_spaces == 0 and command == "out":
        print("Garage is empty")


#Find the bug bug attempts sozunun loopun icinde yazilmasindadir


password = 'secret'
attempts = 0
while True:
    entered = input('Password: ')
    if entered == password:
        print('Welcome')
        break
    attempts+=1
    if attempts==3:
        print("Account locked")
        break


# Password strength


digits = 0
uppercases = 0
lowercases = 0
user_password=input('Enter the password: ')
for i in user_password:
    if i.isdigit():
        digits+=1
    if i.isupper():
        uppercases+=1
    if i.islower:
        lowercases+=1
if len(user_password)>=8 and digits>=1 and uppercases>=1 and lowercases>=1:
    print('Strong password')
else:
    if digits==0 and uppercases==0 and lowercases==0:
       print("Weak password: no digits, no lowercase letters and no uppercase letters")
    elif uppercases==0 and lowercases==0:
        print("Weak password: no uppercase letters and no lowercase letters")
    elif lowercases==0 and digits==0:
        print("Weak password:no lowercase letters and no digits")
    elif uppercases==0 and digits==0:
        print ("Weak passport: no uppercase letters and no digits")    
    elif digits==0:
        print("Weak passport:no digits")
    elif uppercases==0:
        print("Weak passport:no uppercase letters")
    elif lowercases==0:
        print("Weak passport: no lowercase letter")


#Savings goal


savings_goal=1000
saved_money=0
k=0
while saved_money<savings_goal:
    saved_money+=50+k*10
    k=k+1
print(f"Goal reached in month {k} saved money is {saved_money}")


#Read the code
#en kicik 7-e bolunen tek ededi tapir


#Bank account menu


pin='2580'
i=0
starting_balance=1000.00
while i<3:
    user_pin=input('Enter yout PIN: ')
    if user_pin==pin:
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")
        user_choice=input("Enter your choice: ")
        if user_choice=="1":
            print(f"Balance is {starting_balance:.2f}")
            continue
        elif user_choice=="2":
            user_deposit=float(input("Enter deposit amount: "))
            if user_deposit<=0:
                print('Invalid amount')
                continue
            else:
                starting_balance+=user_deposit
                print(f"{starting_balance:.2}")
                continue
        elif user_choice=="3":
            user_withdraw_amount=float(input('Enter the amount you want to withdraw: '))
            if user_withdraw_amount<=0:
                print("invalid amount")
                continue
            else:
                starting_balance-=user_withdraw_amount
                print(f"Balance is {starting_balance:.2f}")
                continue
        elif user_choice=="4":
            print("Goodbye")
            break
    i+=1
if i==3:
    print("Card blocked")


#Vending machine


total_coin=0.00
while total_coin<1.5:
    user_coin=float(input("Insert coin: "))
    if user_coin==0.05 or user_coin==0.10 or user_coin==0.20 or user_coin==0.50 or user_coin==1.0:
        total_coin+=user_coin
        print(f"{total_coin:.2f}")
    else :
        print("Coin is not accepted")
if total_coin>=1.5:
    print("Here is your water")
    print(f"Change: {total_coin-1.5}")


#door codes


c=0
for i in range(2,100):
    k=0
    for a in range(1,i+1):
        if i%a==0:
            k=+1
    if k==2:
        c+=1
        print(i , end=" ")
print(f"Total codes: {c}")

#Read the code 
# 101 102 104
# 201 202 204 
# 301 302 304 

#Hotel room list
for floor in range (1,6):
    if floor==4:
            continue
    print(f"floor {floor}:" , end=" ")
    for room in range (1,5):
        if floor==4:
            break
        print(floor*100+room , end=" ")
    print()


#Bank queue


serving_time=480
time_served=0
i=1
served_customers=0
while time_served<serving_time:
    customer_time=int(input(f"Customer {i} needs (min): "))
    if customer_time+time_served<=serving_time:
       time_served+=customer_time
       served_customers+=1
       i+=1
    else:
        print("Sorry, come back tomorrow")
        break
print(f"Customers served: {served_customers}")
print(f"Minutes left: {serving_time-time_served}")


#Vote counting


loop="start"
A=0
B=0
C=0
Spoiled=0
while loop != "end":
    loop=input("Enter your vote: (A/B/C/END): ")
    match loop:
        case 'A':
            A+=1
        case 'B':
            B+=1
        case 'C':
            C+=1
        case 'end':
            break
        case _:
            Spoiled+=1
            continue
print(f"A: {A} , B: {B} , C:{C}")
print(f"Spoiled: {Spoiled}")
if A>B and A>C:
    print('Winner: A')
elif B>A and B>C:
    print('Winner: B')
elif C>A and C>B:
    print("Winner: C")
else:
    print('Tie')


#Card number check


sum=0
complete=""
while True:
    card=input("Enter card number: ")
    if card.isdigit() and len(card)==16:
        for i in range (15,-1,-1):
            if i%2==0:
                if int(card[i])*2>9:
                    complete+=str(int(card[i])*2-9)
                else :
                    complete+=str(int(card[i])*2)
            else:
                complete+=card[i]
        break
    else:
        print('Must be 16 digits')
        continue
for i in complete:
   sum+=int(i)
if sum%10==0:
    print('Valid number')
else :
    print('Invalid number')


