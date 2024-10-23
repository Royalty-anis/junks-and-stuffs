def vat():
    price = int(input("How much is the item? "))
    vat = (0.15 * price)
    total = f"Total = ${vat + price} "
    return total

def recheck():
    while True:
        vat_recheck = input("Will you like to check any other? Yes/No> ").lower()
        if vat_recheck == 'yes':
            return vat()
        elif vat_recheck == 'no':
            return
        else:
            print("input the right option!")
            return recheck()

try:
    print(vat())
    print(recheck())
except ValueError:
    print("input the right value!")

