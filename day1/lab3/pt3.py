"""
this snippet of code prints all of the sounds exept 'Fa' and 'La.'
"""

"""
phrase = "Do Re Me Fa So La Ti Do"
phraseList = phrase.split()
# note that  phraseList is equal to ['Do', 'Re', 'Me', 'Fa', 'So', 'La', 'Ti', 'Do']
answer = ""
for word in phraseList:
    if word[1] != 'a':
        answer = answer + word
print(answer)
"""

"""
prints it without spaces too.
"""



"""
i would use the .split() function to turn it into an array.
make a new variable called answer ans set it equal to "".
then loop through the array adding the first letter of each string of
the array to the prievious answer.
"""
def acronym(phrase):
    newphrase = phrase.split(" ")
    answer = ""
    for i in range(len(newphrase)):
        answer += newphrase[i][0]
    return answer
print(acronym(input("what do you want to acronymize  >> ")))
