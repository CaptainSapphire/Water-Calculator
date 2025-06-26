import bottles

def bottle_checker(a):
  if (a== "Y") {
    print("Cool!")
  }
  if (a == "N") {
    print("Oh.")
  }

# Explain to user how to find the ounces on the water bottle/cup they drink, maybe make an algorithm based on the name that finds it for them
print("Welcome to the water calculator!")
print("How many bottles do you need to drink a day based on your water bottle? Let's find out.")
#
csv_check = input("First, do you know how many oz/mL your water bottle holds? It is often at the bottom of the bottle, check there! (Y/N)")


# Make it imperial versus metric system
# Maybe make it in metric, and then make a conversion function?
# L, mL = Metric, ounces = imperial

####
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
  print("I'm sorry, I don't understand. I unfortunately cannot run this program without your measurement system.")
}

# water bottle amount
# adjust ounces for system
water_bottle = input("What is the total amount in " + unit + " your water bottle can hold?")

# The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.
# gender is a shorter term than biological sex so thats why the variable is like that
gender = input("What is your biological sex? (F for female, M for male)")

# How much water does a person need in total?
# if sex  is girl
total_needed = 0
if (gender == "F") {
  if (system == "M") {
      total_needed = 0;
  }
  elif (system == "I") {
        total_needed = 0;
    }
}
# if sex is boy
if (gender == "M" {
  if (system == "M") {
        total_needed = 0;
    }
  elif (system == "I") {
        total_needed = 0;
    }
}

# How many bottles of water are they going to drink
bottle_total = total_needed/water_bottle
