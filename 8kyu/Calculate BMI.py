"""
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""


#answer
def bmi(weight, height):
    total_bmi = weight / (height * height)
    if(total_bmi <= 18.5):
        return "Underweight"
    elif(total_bmi <= 25.0):
        return "Normal"
    elif(total_bmi <= 30.0):
        return "Overweight"
    else:
        return "Obese"
