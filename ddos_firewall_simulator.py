request_count = 0
while True:
    command = input("Enter Command: ")
    if command != "CONNECT":
        print("Invaild packet format. Dropping request.")
        continue
    request_count = request_count + 1
    if request_count <= 3 :
        print ("Request procsessed. Load:", request_count, "/3")
    else:
        print("DDoS Attack Detected!")
        break

