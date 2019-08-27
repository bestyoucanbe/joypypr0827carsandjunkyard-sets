# Practice: Showroom & Junkyard
# Create an empty set named showroom.
# Add four of your favorite car model names to the set.
# Print the length of your set.
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Using update(), add two more car models to your showroom with another set.
# You've sold one of your cars. Remove it from the set with the discard() method.
# Acquiring more cars
# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom = set()
showroom = {"Model 3", "Impala", "Murano", "F150"}

# get the length of the showroom set
length_showroom = len(showroom)
print("length of showroom-->", length_showroom)

# Tried to add an <existing element> into the set
showroom.add("Model 3")
print("showroom-->", showroom)

# Add models-->Brackets are necessary to add each item!
showroom.update(["Titan", "Corvette"])

# Remove a car
showroom.discard("Corvette")

junkyard_cars = {"Bel Air", "Nova", "Thunderbird", "Impala", "F150"}

models_in_both = showroom.intersection(junkyard_cars)
print("models in both-->", models_in_both)

# create a set containing all the models from both sets
all_the_cars = showroom.union(junkyard_cars)

# remove the car from the showroom
showroom.discard("Impala")
