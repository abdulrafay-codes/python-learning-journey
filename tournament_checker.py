Age = int(input("Enter the age of the player: "))
if Age < 16:
    print("Sorry, you must be at least 16 years old to register for the tournament.")
else:
    Handicap = int(input("Please enter your current handicap: "))
    if Handicap < 10:
        print("Welcome! You qualify for the Elite division of the tournament.")
    else:
        print("Welcome! You qualify for the Standard division of the tournament.")