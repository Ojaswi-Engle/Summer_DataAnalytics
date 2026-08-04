'''Problem 18: Find uncommon words from two Strings.
Statement: Given two sentences as strings A and B.
 The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. 
 Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters'''

A=input("enter first string:")
B=input("enter second string:")
uncommon=[]

a=A.split()
b=B.split()

all_words=a+b

for word in all_words:
    if all_words.count(word)==1:
        uncommon.append(word)

print(uncommon)
