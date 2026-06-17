balance = 100
for i in range(3):
    amount = int(input("Enter amount to withdraw:"))
    if amount > balance:
        print("Insufficient funds. Try again.")
    else:
        balance = balance - amount
        print("Withdrawal successful. Remaining balance:", balance)
    if balance == 0:
        print("Your account is empty. Goodbye.")
        break
