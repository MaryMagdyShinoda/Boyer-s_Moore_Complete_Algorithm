check = 0
def badChar_preprocess(string, size):
    NO_OF_CHARS = 256
    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # return initialized list
    return badChar


def badChar_useshifts(s, numofshifts):

    if counter < 0:
        print("Pattern occur at shift = {}".format(s))
        s += numofshifts

        global check
        check = 1

    else:
        s += max(1, numofshifts)

    return s


def badChar_getshifts(text, pat, s):

    # for given pattern
    badChar = badChar_preprocess(pat, m)

    j = m - 1

    if (s <= n - m):

       while j >= 0 and pat[j] == text[s + j]:
           j -= 1

       global counter
       counter = j

       if j < 0:

           if s + m < n:
               numofshifts = (m - badChar[ord(text[s + m])])

           else:
               numofshifts = 1

       else:
           numofshifts = j - badChar[ord(text[s + j])]

       return numofshifts


# preprocessing for strong good suffix rule
def goodsuffix_preprocess_case1(shift, bpos, pat, m):
    # m is the length of pattern
    i = m
    j = m + 1
    bpos[i] = j

    while i > 0:

        while j <= m and pat[i - 1] != pat[j - 1]:

            if shift[j] == 0:
                shift[j] = j - i

            # Update the position of next border
            j = bpos[j]

        i -= 1
        j -= 1
        bpos[i] = j


# Preprocessing for case 2
def goodsuffix_preprocess_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):

        if shift[i] == 0:
            shift[i] = j

        if i == j:
            j = bpos[j]


def goodsuffix_useshifts(s, numofshifts):

    if counter < 0:
        print("Pattern occur at shift = {}".format(s))
        s += numofshifts

        global check
        check = 1
    else:
        s += numofshifts

    return s


def goodsuffix_getshifts(text, pat, s):

    bpos = [0] * (m + 1)

    # initialize all occurrence of shift to 0
    shift = [0] * (m + 1)

    # do preprocessing
    goodsuffix_preprocess_case1(shift, bpos, pat, m)
    goodsuffix_preprocess_case2(shift, bpos, pat, m)

    j = m - 1

    if s <= n - m:

        while j >= 0 and pat[j] == text[s + j]:
            j -= 1

        global counter
        counter = j

        if j < 0:
            numofshifts = shift[0]

        else:
            numofshifts = shift[j + 1]

    return numofshifts


# Driver program to test above function
text = "ABCDABCD"
pat = "NNN"

m = len(pat)
n = len(text)

s = 0
while s <= n - m:
    numofshifts1 = goodsuffix_getshifts(text, pat, s)
    numofshifts2 = badChar_getshifts(text, pat, s)

    if (numofshifts1 >= numofshifts2):
        print(numofshifts1, " >= ", numofshifts2)
        print("use number of shifts in good suffix")
        s = goodsuffix_useshifts(s, numofshifts1)

    else:
        print(numofshifts2, " > ", numofshifts1)
        print("use number of shifts in bad char")
        s = badChar_useshifts(s, numofshifts2)

if check == 0:
    print("pattern not found")

print("-----------------------------------------------------------------------------------")

text = "ABCDRRRABCD"
pat = "AB"
m = len(pat)
n = len(text)
s = 0
while s <= n - m:
    numofshifts1 = goodsuffix_getshifts(text, pat, s)
    numofshifts2 = badChar_getshifts(text, pat, s)
    if (numofshifts1 >= numofshifts2):
        print(numofshifts1, " >= ", numofshifts2)
        print("use number of shifts in good suffix")
        s = goodsuffix_useshifts(s, numofshifts1)
    else:
        print(numofshifts2, " > ", numofshifts1)
        print("use number of shifts in bad char")
        s = badChar_useshifts(s, numofshifts2)

if check == 0:
    print("pattern not found")

print("-----------------------------------------------------------------------------------")

text = "ABCDABCDABCD"
pat = "CD"

m = len(pat)
n = len(text)

s = 0
while s <= n - m:
    numofshifts1 = goodsuffix_getshifts(text, pat, s)
    numofshifts2 = badChar_getshifts(text, pat, s)

    if (numofshifts1 >= numofshifts2):
        print(numofshifts1, " > ", numofshifts2)
        print("use number of shifts in good suffix")
        s = goodsuffix_useshifts(s, numofshifts1)

    else:
        print(numofshifts2, " > ", numofshifts1)
        print("use number of shifts in bad char")
        s = badChar_useshifts(s, numofshifts2)

if check == 0:
    print("pattern not found")

print("-----------------------------------------------------------------------------------")

text = "ABCDGGGABCD"
pat = "GGG"
m = len(pat)
n = len(text)
s = 0
while s <= n - m:
    numofshifts1 = goodsuffix_getshifts(text, pat, s)
    numofshifts2 = badChar_getshifts(text, pat, s)
    if (numofshifts1 >= numofshifts2):
        print(numofshifts1, " >= ", numofshifts2)
        print("use number of shifts in good suffix")
        s = goodsuffix_useshifts(s, numofshifts1)
    else:
        print(numofshifts2, " > ", numofshifts1)
        print("use number of shifts in bad char")
        s = badChar_useshifts(s, numofshifts2)

if check == 0:
    print("pattern not found")