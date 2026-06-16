Bill = float(input("Enter your total shopping bill:"))
if Bill >= 5000:
    discount = Bill * 0.2
    Final_Price = Bill - discount
    print("Congratulations! You have received a 20% discount.")
elif Bill >= 2000 and Bill <= 4999:
    discount = Bill * 0.1
    Final_Price = Bill - discount
    print("Congratulations! You have received a 10% discount.")
else:
    print("No discount available.")
    Final_Price = Bill
print("Your final price is:", Final_Price)

