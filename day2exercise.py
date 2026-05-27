age = 10
has_id = False
balance = 0

if age >= 18 and has_id == True and balance >= 1:
    print("you are eligible to open an account")
elif age < 18 and has_id == False and balance < 1:
    print("No requirements met, you do not qualify")
elif age < 18 and balance < 1:
    print("you are underage and have insufficient balance")
elif age < 18:
    print("you are an underage")
elif has_id == False:
    print("Invalid ID")
else:
    print("Insufficient balance")
