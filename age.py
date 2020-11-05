age=1
age=int(input("enter your age: "))
if(age<=18):
    print("you are not allow for driving licence ")
elif(age<=0 or age>=100 ):
    print("you entered invalid input")
else:
    print("you are allow for driving licence ")