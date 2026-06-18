def Weight_Cost(weight, zone_charges):
    if weight < 5:
        print("NO additional cost for weight less than 5 kg.")
        Total_Cost = zone_charges
        return Total_Cost
    elif weight >= 5 and weight <= 20:
        print("Additional cost for weight over 5Kg is $2.00 per Kg.")
        Extra_Weight = weight - 5
        Extra_Cost = Extra_Weight * 2
        Total_Cost = zone_charges + Extra_Cost
        return Total_Cost
    else:
        print("[HEAVY OVERLOAD]")
        print("Extra $5.00 per Kg over 5Kg, plus $20.00 safety handling fee.")
        Extra_Weight = weight - 5
        Extra_Cost = Extra_Weight * 5
        Total_Cost = zone_charges + Extra_Cost + 20
        return Total_Cost
Num_clients = int(input("Enter Number of clients for which data is to be entered: "))
for i in range(Num_clients):
    Zone = input("Where do you want your product to be delivered? (Local, National, International): ")
    if Zone == "Local":
        print("Zone charges: $5.00")
        Zone_charges = 5
    elif Zone == "National":
        print("Zone charges: $15.00")
        Zone_charges = 15
    elif Zone == "International":
        print("Zone charges: $50")
        Zone_charges = 50
    else:
        print("Invalid input. Please enter Local, National, or International.")
        continue
    Weight = float(input("Enter the weight of the product in Kg: "))
    total_cost = Weight_Cost(Weight, Zone_charges)
    if total_cost > 200:
        print("Discount given of 15% for total cost over $200.")
        final_amt = 0.85 * total_cost
        print("Total amount after discount:", final_amt)
    elif total_cost > 100 and total_cost <= 200:
        print("Discount given of 5% for total cost over $100.")
        final_amt = 0.95 * total_cost
        print("Total amount after discount:", final_amt)
    else:
        print("No discount given for total cost less than or equal to $100.")
        final_amt = total_cost
        print("Total amount after discount:", final_amt)

    

