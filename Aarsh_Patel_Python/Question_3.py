'''
3.	Write a program that takes a number (1-100) and determines whether this is a product of two Prime numbers.
If yes, print the two Prime numbers, otherwise print a “try again” message. Allow the user 3 tries.
'''
primenum = []

def findPrime(until):
  for num in range(until+1):
    isPrime = True
    for i in range(num):
        if i != 0 and i != 1 and num % i == 0:
            isPrime = False
        if isPrime and i == num-1:
            primenum.append(num)

findPrime(100)

def checkProduct(product):
    product = int(product)
    for num in range(len(primenum)):
            value = int(product) / int(primenum[num])
            for numb in primenum:
                if value == numb:
                    print(str(primenum[num])+" "+str(numb))
                    return True


    return False



attempts = 3


while attempts>0:
    number = input(str(attempts) + " Enter a product: ")
    if checkProduct(number) == False:
        print("try again")



    attempts -=1
