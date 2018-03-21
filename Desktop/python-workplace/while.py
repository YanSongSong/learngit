#while test
number=23
result=True
while result:
    guess=int(input("Enter an integer:"))
    if guess==number:
        print("Right!")
        result=False
    elif guess>number:
        print("a little higher...")
    else:
        print("a little lower...")
print("done")
