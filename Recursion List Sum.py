def recursive(data_list):
    total = 0
    for ele in data_list:
        if type(ele)==type([]):
            total=total+recursive(ele)
        else:
            total=total+ele  #0+1=1+2=3+3=6+4=10+5+6=21
    return total
print(recursive([1,2,[3,4],[5,6]]))