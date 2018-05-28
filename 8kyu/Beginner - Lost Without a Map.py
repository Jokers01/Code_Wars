"""
Given and array of integers (x), return the array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.
"""

#answer
def maps(a):
    return [ x * 2 for  x in a ]

#or
def maps(a):
    new_list = []
    for x in a:
        new_list.append(x*2)
    return new_list
    
