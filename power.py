num = int(input(" Please Enter the Positive Integer : "))
exponent = int(input("  Enter Exponent Value : "))
power = 1
for i in range(1, exponent + 1):
    power = power * num
    print("The Result of {0} Power {1} = {2}".format(num, exponent, power))
