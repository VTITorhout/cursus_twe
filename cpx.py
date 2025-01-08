import math
def car2pol(a,b):
    #convert carthesian (a+j.b) to polair (mod/arg)
    mod = abs(complex((f"{a}+{b}j")))
    arg = math.degrees(math.atan(b/a))
    return mod,arg
