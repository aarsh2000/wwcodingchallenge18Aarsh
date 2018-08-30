
def checkPalindrome(string):
    backwords = ""
    i = len(string)-1

    while i >= 0:
        backwords = backwords + string[i]
        i -= 1

    answer = True

    for i in range(len(string)):
        if string[i] == backwords[i]:
            answer = True
        else:
            answer = False
            break

    if not(answer):
        return False
    else:
        return True


value_one = 0
value_two = 0
product = 0
for i in range(1000):
    for j in range(1000):
        if i > 99 and j >99:
            number = i * j
            if checkPalindrome(str(number)):
                value_one = i
                value_two = j
                product = number
                print(str(i)+"*"+str(j)+"="+str(product))

print("Therefore highest palindrome is, "+str(product)+" by multiplying "+str(value_one)+" and "+ str(value_two))

