#temperature = int(input("What is your temperature : "))
#if temperature > 80:
#    print("Its too hot!")
#    print("Stay inside!")
#elif temperature < 60:
#    print("It's to cool!")
#    print("Stay inside!")
#else:
#    print("Have a nice day")

name = input("What is your name : ")
mark = int(input("What is your mark : "))
if mark >= 80:
    print("You are briliant")
    grade="A"
elif mark >= 60:
    print("You did okay")
    grade="B"
else:
    print("Better luck next time")
    grade="C"

print("Hi",name,"your mark is",mark,"your grade is",grade)