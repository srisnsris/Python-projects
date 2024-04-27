l1=[1,2,3]
l2=[3,4,5]
l1.append(l2)    #extend(l2)
print(l1)


l1=[1,2,3]
l2=[3,4,5]
l1[:0]=l2
print(l1)
