word = input("Enter word: ")
backwords = ""
i = len(word)-1

while i >= 0:
    backwords = backwords + word[i]
    i -= 1

answer = True

for i in range(len(word)):
    if word[i] == backwords[i]:
        answer = True
    else:
        answer = False
        print("False")
        break

if not(answer):
    print("Not palindrome")
else:
    print("Is palindrome")

