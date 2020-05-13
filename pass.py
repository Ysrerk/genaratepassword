import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","w","y","z"]
cletter=[]
password=[]
for i in letter:
    cletter.append(i.upper())

chareckter=["@","*","_","!","/","&"]
numbers=list(range(0,10))

passcharnumber=int(input("Please write how many charecter do you want include in your password\n"
                         "Note:it should be between 6 and 10 digit\n"))
if 6<= passcharnumber<=10:
    if passcharnumber==6:
        password.append(random.sample(cletter,1))
        password.append(random.sample(numbers,2))
        password.append(random.sample(letter,1))
        password.append(random.sample(chareckter,2))
    elif passcharnumber==7:
        password.append(random.sample(cletter,1))
        password.append(random.sample(numbers,2))
        password.append(random.sample(letter,2))
        password.append(random.sample(chareckter,2))
    elif passcharnumber==8:
        password.append(random.sample(cletter,1))
        password.append(random.sample(numbers,3))
        password.append(random.sample(letter,2))
        password.append(random.sample(chareckter,2))
    elif passcharnumber==9:
        password.append(random.sample(cletter,1))
        password.append(random.sample(numbers,3))
        password.append(random.sample(letter,3))
        password.append(random.sample(chareckter,2))
    elif passcharnumber==10:
        password.append(random.sample(cletter,1))
        password.append(random.sample(numbers,4))
        password.append(random.sample(letter,3))
        password.append(random.sample(chareckter,2))
else:
    print("please write between 6 to 10")
#####Password writing screen
print("Your Password is ready :\n")
for i in password:
    for j in i:
        print (j,end="")
