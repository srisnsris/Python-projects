C = 2   #global, can re use anywhere
def Claim():
    NPI= 12345      #local var should use func
    TAX= 123456
    #Taxo = "SX123"
print(Claim.__code__.co_nlocals)