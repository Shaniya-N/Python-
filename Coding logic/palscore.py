# Given a space seperated string.Calculate the score of the string.Score is determined
# as follows; if the word is a palindrome and the word length is 4,add 5 to the score.
#             if the word is a palindrome and the word length is 5,add 10 to the score
#             if the word is not palindrome,add 0 to the score.
# input: asdfg htth jklm rrtrr qwerty
# output: 15

a=input().split()
def ispalindrome(i):
        if i[:]==i[::-1]:
            return True
score=0       
for i in a:
    if ispalindrome(i):
        if len(i)==4:
            score+=5
        elif len(i)==5:
            score+=10
    else:
         score+=0
print(score)