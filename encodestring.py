def encode(s):
    c = ''
    t = 0
    itr = 0
    res = ''
    while itr < len(s):
        c = s[itr]
        t = 1
        while s[itr] == c and itr + 1 < len(s):
            t += 1
            itr += 1
        res += str(t) + c
        itr += 1
    return res
print(encode('aaajjhhukjjhggggg'))