'''we can make a block of code execute over and over again using a while 
statement.the code in this while clause will be executed as long as the
while statement's condition is true'''

#example with if statement
a=0
if a<5:
    print("a is less than 5")
    a=a+1
print(a) #a becomes 1 but the loop is not exected again

#example with a while loop
b=0
while b<5:
    print("b is less than 5")
    b=b+1
print(b) #this while loop is executed untill the value of b<5 and stopsat b=5