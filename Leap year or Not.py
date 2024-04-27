def checkyear(year):
    return((( year % 4==0) and (year % 100 !=0)) or (year%400==0))  # ((T and F=false) as F) or T=T
year=2000
if(checkyear(year)):
    print('leap year')
else:
    print("Not a leap year")