import math
# import math is for using pi
#import time for time.sleep later

## FUNCTIONS
def calc_volume():
  print("Looks like we will calculate that ourselves.")
  # step one: find the circumference
  print("The first step is to find the circumference, which we can either use the diameter for, or you can measure by wrapping a measure around the bottle and recording the amount.")
  conditional = input("If you would like to measure the circumference yourself, please reply C. If you would like to use diameter instead, reply D.")
  if (conditional == "C"):
    circumference = float(input("What is the circumference of your bottle in " + height_units + "?"))
  elif (conditional == "D"):
    print("The diameter of the bottle is from one point to another, going through the center. ")
    diameter = float(input("What is the diameter?"))
    circumference = diameter * math.pi
  else:
    print("Invalid input.")
  # step two: radius
  radius = circumference / (2 * math.pi)

  # step three: height
  height = float(input("What is the height of your bottle in" + height_units))

  # step four: volume
  volume = radius ^ 2 * height * math.pi

  # step five: units
  # it will be in cubic inches, will move to ounces
  # cubic centimeters are the same thing as mL so no conversions for the metric system users 

################################
## START
# Explain to user how to find the ounces on the water bottle/cup they drink, maybe make an algorithm based on the name that finds it for them
print("Welcome to the water calculator!")
print("How many bottles do you need to drink a day based on your water bottle? Let's find out.")

## SYSTEM OF MEASUREMENT
# Make it imperial versus metric system
# Maybe make it in metric, and then make a conversion function?
# L, mL = Metric, ounces = imperial
unit = ""
system = input("Are you in the imperial or metric system? (I=imperial, M= Metric)")

if (system == "I"):
  print("imperial")
  unit = "ounces"
  height_units = "inches"

elif (system == "M"):
  print("Metric")
  unit = "mL"
  height_units = "centimeters"

else:
  # Make this loop the system input
  print("I'm sorry, I don't understand. I unfortunately cannot run this program without your measurement system.")


## BOTTOM OF BOTTLE
bottom_bottle = input("Do you know how much water your bottle can hold? (Typically listed on the bottom of the bottle or on website purchased) Y or N.")

# consider the units being used
if (bottom_bottle == "Y"):
  water_bottle = input("What is the total amount in " + unit + " your water bottle can hold?")
elif (bottom_bottle == "N"):
  calc_volume()

else:
  # Make this loop the system input
  print("Invalid input.")


## USER DATA 
# The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.
# gender is a shorter term than biological sex so thats why the variable is like that
gender = input("What is your biological sex? (F for female, M for male)")

# How much water does a person need in total?
# if sex is female
total_needed = 0
if (gender == "F"):
  if (system == "M"):
      total_needed = 0;
  
  elif (system == "I"):
        total_needed = 0;
    
# if sex is male
if (gender == "M"):
  if (system == "M"):
        total_needed = 0;
  elif (system == "I"):
        total_needed = 0;

# consider age 


# FINAL BOTTLE CALCUATION
# How many bottles of water are they going to drink
bottle_total = total_needed/water_bottle
