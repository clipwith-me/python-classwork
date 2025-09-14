def large_power():
    base = input("Enter the base number: ")
    exponent = input("Enter the exponent number: ")


    if int(base) ** int(exponent) > 5000:
        return True
    else:
        return False

def divisible_by_ten():
    num = input("Enter a number: ")
    if int(num) % 10 == 0:
        return True
    else:
        return False