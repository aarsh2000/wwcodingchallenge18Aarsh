import string

st = input("Enter value:")

asc=[]

for i in range(130):
    asc.append(0)



for letter in st:
    for number in range(130):
        if ord(letter) == number:
            asc[number]+=1
            


            
highest = 0
index = 0

for num in range(130):
    if asc[num] >= highest:
        highest = asc[num]
        index = num

print(chr(index))


