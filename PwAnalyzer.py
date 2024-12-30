import string
import re
FeedBack=[]
PwScore=0
# input, length, and commonalities check
while True:
 password= input("enter your password: ")
 with open('10-million-password-list-top-1000000.txt','r') as f:
    common = f.read().splitlines()
    if password not in common: 
        print("password is acceptable.  ") 
        break
    else:
        print("password is too common, try again. ")
    
    
if len(password)<8: 
    FeedBack.append("pw length is too short.")
elif len(password)>=12:
    PwScore+=2 ; FeedBack.append("great length!")
else: PwScore+=1 ; FeedBack.append("moderate length.")
#regex search

if  re.search(r'[A-Z]', password): FeedBack.append("contains uppercase " ) ; PwScore+=1
else: FeedBack.append("must contain capital letter. ")


if re.search(r'[a-z]', password):
    FeedBack.append("password contains lowercase letter ") ; PwScore+=1
else: FeedBack.append("must contain a lowercase letter.")


if re.search(r'(?:\D*\d){4}', password):
    FeedBack.append("password contains 3 or more digits. acceptable ") ; PwScore+=3
elif re.search(r'(\d.*?){3}', password):
    FeedBack.append("password contains 3 digits. requirement met. ") ; PwScore+=3
elif re.search(r'(\d.*?){2}', password):
    FeedBack.append("password contains 2 digits. 1 more is required. ") ; PwScore+=2
elif re.search(r'(\d.*?){1}', password):
    FeedBack.append("password contains more than 1 digit, 2 more is required. ") ; PwScore+=1
else: FeedBack.append("password must contain 3 or more digits. ")

if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    FeedBack.append("password contains a special character. ") ; PwScore+=1
else: FeedBack.append("password needs atleast one special character. ")


print(f"your pw score is: {PwScore}/8 ")
print("system feedback: ")
for item in FeedBack:
    print(f"-{item} " )
    


    










