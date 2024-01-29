import random
words = input("Your Text: ").split(" ")
mow = "" #middleOfWord
cw = "" #currentWord
atw = "" #addToWord
cw_len = 0
wpl = 15 #wordsPerLine
for i in range(len(words)):
    cw = words[i]
    cw_len = len(cw)
    atw = " "
    if(cw_len > 1):
        if(cw.endswith((",", ".", "!", "?"))):
            atw = cw[cw_len-1] + atw
            cw = cw[0:cw_len-1]
            cw_len -= 1
        mow = cw[1:cw_len-1]
        words[i] = cw[0]+''.join(random.sample(mow,len(mow)))+cw[cw_len-1]+atw
    else:
        words[i] = cw + atw
for a in range(0,len(words),wpl):
    print(''.join(words[a:a+wpl]))