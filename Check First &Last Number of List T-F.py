numbers_x=[10,20,30,40,10]   #50
def first_last(numbers_x):
    first = numbers_x[0]
    last = numbers_x[-1]
    if first == last:
        return True    #if we are using return need ot use print
    else:
        return False
    
print(first_last(numbers_x))


