'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''

def rew_word(s):
    words=[]
    length=len(s)
    spaces=[' ']
    i=0
    while i<length:
        if s[i] not in spaces:
            word_start=1
            while i<length and s[i] not in spaces:
                i+=1
                if s[i-1] not in spaces:
                    words.append(s[word_start:i])
            i+1
        return "".join(reversed(s))
print(rew_word("SMS hello     five"))