"""
Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:

If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
How much is Michael going to pay? Calculate the amount with two decimals, if necessary.

"""


#answer
def michael_pays(costs):
    if(costs < 5):
        return round(costs,2)
    else:
        t=costs * 1/3
        if t > 10:
            return round(costs -10 ,2)
        return round(costs - t ,2)

#or
def michael_pays(costs):
    if(costs < 5):
        return round(costs,2)
    elif(costs * 1/3 > 10):
        return round(costs -10 ,2)
    return round(costs-(costs * 1/3),2)
