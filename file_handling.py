fhandle = open("email.txt",'w')
fhandle.write("Important: Meeting at 3 PM\n")
fhandle.write("Winner! Claim your free vacation now\n")
fhandle.write("Project update and notes\n")
fhandle.write("URGENT: Click here to change password\n")
fhandle.write("Hey, are we still on for dinner?\n")
fhandle.close()
cleanfile = open("clean_inbox.txt", "w")
fhandle = open("email.txt")
for line in fhandle:
    if not "Winner!" in line and not "URGENT:" in line:
        cleanfile.write(line)
cleanfile.close()
cleanfile = open("clean_inbox.txt")
for line in cleanfile:
    print(line.rstrip())
     
    
