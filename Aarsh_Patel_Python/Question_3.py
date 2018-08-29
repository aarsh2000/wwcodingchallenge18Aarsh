primenum = []
product = []
for i in range(10):
    product.append(0)
    
def prime(num):
    for i in range(num):
        if i!= 0 and i!= num and i!= 1:
            if  num%i==0:
                return True
            else:
                return False
    

for i in range(100):
    if prime(i) == False:
         primenum.append(i)
    
for i in range(len(primenum)):
    for j in range(len(primenum)):
        product.append(primenum[i]*primenum[j])
        


attempts = 3

answer = False
while attempts>0:
    number = input(str(attempts) + " Enter a value: ")
    for i in range(len(product)):
        if number == product[i]:
            answer = True
        else:
            answer = False

    if answer:
        print("yes")
    else:
        print("try again")
         
    attempts -=1
