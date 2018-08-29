import string

st = input("Enter value:")

asc=[]

for i in range(130):
    asc.append(0)



for letter in st:
    for number in range(130):
        if ord(letter) == number:
            asc[number]+=1
            


upperCase = 0
lowerCase = 0
            
for num in range(130):
    if num>=60 and num<=90 and asc[num]>0 :
        upperCase+=1
    elif num>=97 and num<=122 and asc[num]>0:
        lowerCase+=1
print("Uppercase: ")
print(upperCase)
print("Lowercase: ")
print(lowerCase)
