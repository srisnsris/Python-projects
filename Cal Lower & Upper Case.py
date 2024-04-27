def string_test(s):
    d = {'upper_case':0,"Lower_case":0}
    for i in s:
        if i.isupper():
            d['upper_case']+=1
        elif i.islower():
                d['Lower_case']+=1
        else:
           pass
    print("Upper Case Letters:",d["upper_case"])
    print("Lower case Letters:",d["Lower_case"])
string_test("SrinivaS VuppalA")
        
            