"""
Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.
"""

#answer
def combat(health, damage):
    t = health - damage
    return t if t > 0 else 0

#or
def combat(health, damage):
    t = health - damage
    if t < 0:
        return 0
    else:
        return t
