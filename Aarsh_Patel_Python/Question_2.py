sentence = input("Enter value: ")

w = sentence.split()

if len(w) == 1:
    print(0)
else:
    lastWord = w[len(w)-1]

    print(len(lastWord))
    

