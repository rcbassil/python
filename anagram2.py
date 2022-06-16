#!/usr/bin/python3

def anagramSolution2(s1,s2):

    alist1 = list(s1)
    alist2 = list(s2)

    if len(alist1) != len(alist2):
        return False

    alist1.sort()
    alist2.sort()

    print(alist1)
    print(alist2)

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))
