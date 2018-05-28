"""
The function is not returning the correct values. Can you figure out why?

get_planet_name(3) # should return 'Earth'

"""



#answer
def get_planet_name(id):
    # This doesn't work; Fix it!
    switches = {
         1: "Mercury",
         2: "Venus",
         3: "Earth",
         4: "Mars",
         5: "Jupiter",
         6: "Saturn",
         7: "Uranus"  ,
         8: "Neptune"
         }
    return switches[id]

#or
def get_planet_name(id):
    # This doesn't work; Fix it!
    switch =  {
         1: "Mercury",
         2: "Venus",
         3: "Earth",
         4: "Mars",
         5: "Jupiter",
         6: "Saturn",
         7: "Uranus"  ,
         8: "Neptune"
         }
    return switch.get(id, None)
