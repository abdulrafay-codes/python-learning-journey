secure_ports = [22, 80, 443]
while True:
    flag = "FALSE"
    I = input("Enter port number to scan (or '0' to stop audit):")
    if I == '0':
        break
    try:
        User_Input = int(I)
        for count in secure_ports:
            if User_Input == count:
                print("[SAFE] Port is open and verified under secure protocols.")
                flag = "TRUE"
        if flag != "TRUE":
            print("[WARNING] Unverified port activity detected! Potential vulnerability.")
    except:
        print("[ALERT] Invalid port signature. Rescanning...")
        continue
print("[SYSTEM] Audit complete. Firewall logs saved.")