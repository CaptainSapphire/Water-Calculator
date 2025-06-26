# Explain to user how to find the ounces on the water bottle/cup they drink, maybe make an algorithm based on the name that finds it for them

# Make it imperial versus metric system
# Maybe make it in metric, and then make a conversion function?
# L, mL = Metric, ounces = imperial

system = input("Are you in the imperial or metric system? (I=imperial, M= Metric)")

if (system = "I") {
  print("imperial");
  unit = "ounces";
}
elif (system = "M") {
  print("Metric");
  unit = "mL";
}
else {
  # Make this loop the system input
  print("I'm sorry, I don't understand. I unfortunately cannot run this program without your unit of measurement.")
}

# water bottle amount
# adjust ounces for system
water_bottle = input("What is the total amount in " + unit + " your water bottle can hold?")

# The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.
gender = input("What is your biological sex? (F for female, M for male)")

# How much water does a person need in total?
total_needed = 0
if (gender = "F") {
  total_needed = 2.7;
}
if (gender = "M" {
 total_needed = 3.7
}

# How many bottles of water are they going to drink
bottle_total = total_needed/water_bottle
