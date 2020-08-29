def mult(x, y):
    result_mult = 0
    i = 0
    while i < y:       # Here I choose 'y'  (witch is the base) to show how many times 'x' going to be sum with itself.
        i += 1
        result_mult += x 

    return result_mult

def expo():
    base = int(input("Type a base: "))
    expo = int(input("Type an exponent: "))
    if base < 0 or 0 > expo:
        print("Don't type any negative value, please try again.")
    else:
        result_expo = 1
        if expo == 0:     #  If the exponent is equal 0 the result number going to be '1'.
            print(f"{base} ^ {expo} = {result_expo}".format(base,expo,result_expo))
        else:
            i = 0
            while i < expo:
                i += 1
                result_expo = mult(result_expo, base)       # result_expo is being multiplied by the base, it's the same thing as ( result_expo * base  )
            print(f"{base} ^ {expo} = {result_expo}".format(base,expo,result_expo))

expo()
