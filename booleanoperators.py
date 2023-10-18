#there are 3 boolean operators respectively(and,or,not)

#AND operator return true only if both operations are true
#example for and operator
a=100
b=200
c=300
print(a<b and b<c)  # true and true retuns true
print(a>b and b>c)  #false and true returns false
print(a<b and b>c)  #true  and false returns false
print(a>b and b>c)  #false and false returns false

#OR operator return true even if one operation is true
print(a<b or b<c)   #true or true returns true
print(a<b or b>c)   #true or false returns true
print(a>b or b<c)   #false or true returns true
print(a>b or b>c)   #false or false returns false

#not operator

a=not True
print(a)         #returns false
b=not False
print(b)         #returns true