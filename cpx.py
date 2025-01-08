def car2pol(a,b):
    #convert carthesian (a+j.b) to polair (mod/arg)
    car = complex(f"{a}+{b}j")
    return abs(car)
