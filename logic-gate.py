# def AND (a, b):
#     if a == 1 and b == 1:
#         return 1
#     else:
#         return 0
    
# def NAND (a, b):
#     if a == 1 and b == 1:
#         return 0
#     else:
#         return 1
    
# def OR(a, b):
#     if a == 1 or b ==1:
#         return 1
#     else:
#         return 0
    
# def XOR (a, b):
#     if a != b:
#         return 1
#     else:
#         return 0
    
# def NOT(a):
#     return not a

# def NOR(a, b):
#     if(a == 0) and (b == 0):
#         return 1
#     elif(a == 0) and (b == 1):
#         return 0
#     elif(a == 1) and (b == 0):
#         return 0
#     elif(a == 1) and (b == 1):
#         return 0
    
# def XNOR(a,b):
#     if(a == b):
#         return 1
#     else:
#         return 0
    
#####

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

######

for i in range (2) :
    for  j in range (2):
        print(i , "|", j , "=" , int (NAND(i,j)))