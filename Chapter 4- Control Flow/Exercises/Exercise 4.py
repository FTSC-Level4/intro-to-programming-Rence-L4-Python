# Stages of Life

## Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
## •If the person is less than 2 years old, print a message that the person is a baby.
## •If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
## •If the person is at least 4 years old but less than 13, print a message that the person is a kid.
## •If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
## •If the person is at least 20 years old but less than 65, print a message that the person is an adult.
## •If the person is age 65 or older, print a message that the person is an elder.


##### Attempt
### Variable-only
print("[Variable only]")
age=18

if age<2:
    print("You are a baby.")
elif age<4:
    print("You are a toddler.")
elif age<13:
    print("You are a kid.")
elif age<20:
    print("You are a teenager.")
elif age<65:
    print("You are an adult.")
else:
    print("You are an elder.")

print("\n\n")


### Stages of Life, Tool using input function
print("[Personal Activity]: Tool")
print("This tool will put you in a group according to your age.")
age=float(input("Enter your age:"))

if age<2:
    print("You are a baby.")
elif age<4:
    print("You are a toddler.")
elif age<13:
    print("You are a kid.")
elif age<20:
    print("You are a teenager.")
elif age<65:
    print("You are an adult.")
else:
    print("You are an elder.")

exit()