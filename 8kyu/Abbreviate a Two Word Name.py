"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

"""

#answer
def abbrevName(name):
    a = list(name.split(" ")[0][0])
    b = list(name.split(" ")[1][0])
    c =''.join(a)+"."+''.join(b)
    return c.upper()
    
