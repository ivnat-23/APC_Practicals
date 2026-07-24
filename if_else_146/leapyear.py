year=int(input("Enter the year:"))
if(year%400==0)or(year%4==0 and year%100!=0):
         print("the year is leap year")
else:
       print("the year isnt leap year")