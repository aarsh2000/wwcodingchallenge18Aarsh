#fibonaci sequence
bound = input("Enter maxima cap of sequence: ")
p_num = 1
p_numtwo = 1
i = 0
def add(limit):
    global p_num
    global p_numtwo
    global i
    if p_num <= limit:
        print(p_num)
    if p_num > limit:
        print(str(i) + " iterations bounded to limit "+str(bound))
    else:
        sum = p_num + p_numtwo
        p_numtwo = p_num
        p_num = sum
        i += 1
        add(limit)



add(int(bound))
