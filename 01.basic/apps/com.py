a = input("Enter a number (No Space):")

a = float(a)

if a > 0 :
    data = "This is a Positive Number"
elif a < 0:
    data = "This is a Negative number"
elif a == 0:
    data = "The number is Zero"

print(data)