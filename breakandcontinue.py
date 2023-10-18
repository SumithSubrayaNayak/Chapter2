#example

while True:
    print("who are you?")
    name=input()
    if name != "Sumith":
        continue     #keeps returning to the start until name is Sumith
    print("hello,Sumith. what is your password?")
    password=input()
    if password=="70196":
        break      #returns to the who are you? if password is wrong
    
print("access granted")