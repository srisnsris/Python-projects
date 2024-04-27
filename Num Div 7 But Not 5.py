l =[]
for i in range(0,50):
    if i%7==0 and i%5!=0:
        l.append(str(l))
        
print(','.join(l))