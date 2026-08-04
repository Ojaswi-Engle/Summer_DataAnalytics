'''Problem 19: Word location in String.
Statement: Find a location of a word in a given sentence.

Example 1:

Input:

Sentence: We can learn data science through campusx mentorship program.

word: campusx
Output:

Location of the word is 7.
Note- Don't use index/find functions


'''

s=input("Sentence:")
word=input("word:")
l=s.split()

if word in l:
    
    location=0
    
    for w in l:
        location+=1
        if w==word:
            print("Location of the word is ",location,'.',sep='')
            break
else:
    print("word is not present")
        
