key=str(input("Enter Your Email "))
n=len(key)
for i in range(0,n+1):
    if(key[i]=='@'):
        flag=i
        break;
if(key[flag+1]=="g" or key[flag+1]=="G"):
    print("Domain : Google (GMAIL)")
elif(key[flag+1]=="y" or key[flag+1]=="Y"):    
    print("Domain : Yahoo! (YAHOO)")
elif(key[flag+1]=="o" or key[flag+1]=="O"):    
    print("Domain : Microsoft (OUTLOOK)")
else:
    print("Your Email not in the List")
    
