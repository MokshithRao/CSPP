word1=input()
word2=input()

def first(word1):
    d1={}
    for i in word1:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    return d1


def second(word2):
    d2={}
    for i in word2:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    return d2


def anagram(word1, word2):
    return first(word1)==first(word2)
print(anagram(word1,word2))
    


