#prime number
bound = input("Enter Enter maxima cap of sequence: ")
count = 0
def prime(limit):
    global count
    for j in range(limit+1):
        for i in range(j):
            if i != 0 and j%i==0 and i != 1:
                j+=1
            if i == j-1:
                count += 1
                print(j)
    print(str(count)+" iterations")
prime(int(bound))
