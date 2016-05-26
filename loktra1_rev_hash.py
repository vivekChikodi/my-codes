def rev_hash(h):
    h1 = h
    str_arr = []
    rem = 0
    letters = "acdegilmnoprstuw"
    while h1 > 37:
        rem = h1%37
        str_arr.append(letters[int(rem)])
        h1 = h1/37
    str_arr.reverse()
    str1 = ''.join(str(e) for e in str_arr)
    return str1

h = int(input('Enter the Hash value: '))
s = rev_hash(h)
print ("The required string is : %s"%s)
