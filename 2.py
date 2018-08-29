string=input("Enter a string:")
length = len(string)
s2 = string.capitalize()
print(s2)
for a in range(0,length):
    print(a)
    if ord(string[a])==ord(" "):
        string[a+1].upper()
print(string) 
print(s2)       
    