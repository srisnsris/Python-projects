l1=[1,2,3]
l2=[4,5,6]
print("original list")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)    #x, y is argument X+y expression
print("result")
print(list(result))