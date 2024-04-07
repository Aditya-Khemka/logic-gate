def AND (a, b):
    return (a and b)
    
def NAND (a, b):
    return (not(a and b))
    
def OR(a, b):
    return (a or b)
    
def NOR (a, b):
    return(not(a or b))
    
def NOT(a):
    return not a

def XOR(a, b):
    return((a and (not b)) or (b and (not a)))
    
def XNOR(a,b):
    return((a and b) or ((not a)and (not b)))