# Conditionals

# setting a variable to True
torch_lit = True

if torch_lit: # if torch_lit == True, if torch_lit is a truthy value
    print("Venture forth into the cave!") # will only print if torch_lit is True

# using a condition for an equality check
# == to check for equality
weather = "sunny"

if weather == "sunny":
    print("Lets go on a picnic!")

# if something is not equal!
# checking if weather does not equal rainy
# it is true that weather does not equal rainy
if weather != "rainy":
    print("Cool beans, we can do something outside today!")


# Combining conditional statements
# with and both conditions need to be true in order for it to be interpreted as true
gold_coins = 10
silver_coins = 50

if gold_coins > 5 and silver_coins > 30:
    print("We have enough to buy the magic potion.")

# make sure you're using the variable on both sides of the and
# DONT DO THIS:
# if gold_coins > 5 and < 15:
#     print("We should keep these coins in our pocket for now.")

# DO THIS
if gold_coins > 5 and gold_coins < 15:
    print("We should keep these coins in our pocket for now.")

# != not equal
enemy = "goblin"
if enemy != "dragon":
    print("Charge forward, you can take on anything thats not a dragon!")

# <= less than or equal to
player_health = 75
if player_health <= 100:
    print("Drink a health potion for full strength!")

# >= greater than or equal to
player_health = 150
if player_health >= 150:
    print("Eh, you're fine you have enough health for now.")

# checking if something fits with in range of two numbers
magic_stones = 9
if 10 <= magic_stones <= 20:
    print("You have enough stones to open the chest!")

# Negative Checks using not

is_daytime = False
dragon_asleep = True
# if is_daytime == False and dragon_asleep == True
if not is_daytime and dragon_asleep:
    print("Try sneaking into the Dragon's layer for some dank lootz.")



# ELIF - allows us to account for additional conditions following the if
# ELIF == ELSE IF
# you cannot have an elif without an if
moon_phase = "full moon"
# adding an elif to an if extends the chain of possibilities
# after something is True, the chain stops
if moon_phase == "full moon":
    print("Beware of werewolves!")

elif moon_phase == "new moon":
    print("Vampires shall sparkle!")


spooky_thing = "Ghost"
print(spooky_thing)
# two if statements will check separately
if moon_phase == "full moon":
    print("Beware of werewolves!")
    spooky_thing = "Werewolf"

if moon_phase == "full moon":
    print("Vampires shall sparkle!")
    spooky_thing = "Vampire"

print(spooky_thing)

# checking potion strength
potion_strength = 15

if potion_strength > 20:
    print("Its a super potent potion")
elif potion_strength > 10:
    print("Its a moderately potent potion")

potion_strength = 9
# the order of the conditionals matters because
# as soon as something evaluates to True the conditional chain stops
if potion_strength < 20:
    print("That is a super potent potion")
elif potion_strength < 10:
    print("That is not a very potent potion")

if potion_strength < 10:
    print("Thats not a very potent potion")
elif potion_strength < 20:
    print("Thats a moderately potent potion")

# Chaining together SEVERAL elifs in a single condition chain
weather = "rainy"

if weather == "sunny":
    print("Lets go play basketball")
elif weather == "rainy":
    print("Stay inside")
elif weather == "snowy":
    print("Time to build a snowman")
elif weather == "cloudy":
    print("stay inside")
elif weather == "tornadoee":
    print("stay inside")


# checking sword quality
sword_material = "silver"

if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("That sword is great for killing werewolves and vampires")
elif sword_material == "bronze":
    print("That sword looks old and crusty.")

# using comparison operators and a range within the elif
player_level = 12

if player_level < 5:
    print("You may access the weenie hut jr. dungeon")
# range if 5 is less than or equal to the player level
# player_level is less than 10
# if player_level >= 5 and player_level < 10:
elif 5 <= player_level < 10:
    print("You may enter the itermediate dungeon")
elif player_level >= 10:
    print("You are prepared to take on the advanced dungeon.")

# ELSE - cover any condition not accounted for with the ifs and elifs
# if none of the previous conditions are True then the else gets hit

# Checking Sword quality
sword_material = "iron"

if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("That sword is great for killing werewolves and vampires")
elif sword_material == "bronze":
    print("That sword looks old and crusty, but will get the job done")
else:
    print("Ehhh I wouldn't bring that sword with me on an adventure. You're better off with a butter knife...")

# using the else with a user input to make sure the correct response is collected
# response = input("Would you like to continue, yes or no?")
# if response == "yes":
#     print("Continuing program")
# elif response == "no":
#     print("quitting program")
# else: 
#     print("Please enter a valid response")

# = is for setting a variable equal to something
# == is for checking equality
is_dragon_present = True
has_treasure = True

# if is_dragon_present == True and has_treasure == False
if is_dragon_present and not has_treasure:
    print("Enter with caution! Dragon ahead, but no treasure in sight")
# is_dragon_present == False and has_treasuire == True
elif not is_dragon_present and has_treasure:
    print("The Dragons not home, come grab his stuff!")
# if is_dragon_present == True and has_treasure == True
elif is_dragon_present and has_treasure:
    print("The dragon guards his hoard. Tread lightly.")
else:
    print("The lair is empty and this dragon is broke af, no treasure here.")

# combining potions
red_potion = True
blue_potion = True
if red_potion and not blue_potion:
    print("You got a potion of strength!")
elif not red_potion and blue_potion: 
    print("You got a potion of speed")
elif red_potion and blue_potion:
    print("OOPS! Dont mix your potions, they explode. d6 fire damage")
else:
    print("You have no potions to use.")

# finding the best path
is_daytime = False
is_raining = True

if is_daytime and not is_raining: 
    print("Take the sunny path through the meadow and do some frolicking")
elif is_raining and is_daytime:
    print("Take the dank, musty path through the swamp.")
else:
    print("Neither path is suitable right now. Use your compass and head back home.")


# Write a chain of conditionals to check which weapon the character is using
# spear, bow, sword, axe
# based on the weapon, print a string explaining what the character can do with that weapon
# for example, if they have a bow, they may attack enemies in the distance
weapon = "bow"


weapon = "spear"
if weapon == 'mace':
    print('you can do some bludgeoning with that!')
elif weapon == 'knife':
    print('you can do some backstabbing with that for sure')
elif weapon == 'staff':
    print('you can cast some sick spells with that!')
elif weapon == 'sword':
    print('so vanilla, boring')
else: 
    print('idk what that is hope its sharp.')

# weapon = "butterknife"
# weapon = "scissors"
weapon = "chopsticks"
# weapon = "bow"
if weapon == "butterknife":
    print("close but no cigar!")
elif weapon ==  "scissors":
    print("this isn't paper")
elif weapon == "chopsticks":
    print("no takeout")
else:
    print("robinhood")

weapon = "bow"
if weapon == "sword":
    print("Able to slash enemies in a short distance")
elif weapon == "spear":
    print("Able to stab enemies from a far distance")
elif weapon == "bow":
    print("Flying arrows can attack enemies from an extreme distance")
else: 
    print("Not familiar with that weapon...")


weapon = "axe"
if weapon == "spear":
    print("For medium range.")
elif weapon == "sword":
    print("For short distance combat")
elif weapon == "bow":
    print("For long distance shots")
elif weapon == "axe":
    print("For spinning attacks")
else: 
    print("You dont have a very good weapon")


# checking user input
# light_color = input("Enter the traffic light color (red, yellow, green)")

# if light_color == "red":
#     print("STOP!")
# elif light_color == "yellow":
#     print("Shout YOLO and floor it through the intersection")
# else:
#     print("GO!")

# refining our conditionals to capture possibilities that are not red, yellow, or green
# if light_color == "red":
#     print("STOP!")
# elif light_color == "yellow":
#     print("Shout YOLO and floor it through the intersection")
# # adding an elif for green
# elif light_color == "green":
#     print("GO!")
# # what happens if one of the colors isnt selected
# else:
#     print("That is not a valid color, please try again!")


# collecting user input to check what movie rating theyd like to see
# and collecting an age input to see if they are old enough for that movie
# age = int(input("Enter your age: "))
# rating = input("Enter a movie rating: (G, PG, PG-13, R): ")
# if rating == "G":
#     print("You can watch the movie!")
# elif rating == "PG" and age >= 7:
#     print("You can watch the movie!")
# elif rating == "PG-13" and age >= 13:
#     print("You can watch the movie!")
# elif rating == "R" and age >= 17:
#     print("You can watch the movie!")
# else:
#     print("You are not allowed to watch this movie")


# Checking how people take their coffee
# Coffee, a beloved beverage for many, is as diverse as the palates of those who drink it. 
# From the rich and creamy lattes to the bold and robust black coffees, 
# there's a perfect brew for everyone. But with so many options, how does one decide? 
# Recommend a type of coffee based on user preferences about sweetness and milk.

# create user inputs for checking if the user likes sugar in their coffee and if they like milk in their coffee
# based on their choices, write conditionals to recommend a type of coffee if they like milk, sugar, both, or neither

# sugarq = input("Do you like sugar in your coffee? Yes/No")
# milkq = input('Do you like milk in your coffee? Yes/No')
# if sugarq == "yes" and milkq == "yes":
#     print("you can get a french vanila latte")
# elif sugarq == "yes" and milkq == "no":
#     print("you can get a black coffee")
# elif sugarq == "no" and milkq == "yes":
#     print("you can get a matcha")
# else: 
#     print("you can get a plain black coffee")


# calculating a fine for overdue library books
# days_overdue = int(input("How many days is the book overdue? "))
# fine = 0

# if days_overdue <= 5:
#     fine = days_overdue * 1
# elif days_overdue <= 10:
#     fine = days_overdue * 2
# else:
#     fine = days_overdue * 5
# # f-string - formatted string
# print(f"Your fine is ${fine}")
# print("Your fine is", fine)

# NESTED CONDITIONALS
temperature = 15
if temperature < 25:
    print("It's a bit chilly")
    # this conditional only runs, if the previous condition is try
    if temperature < 15:
        print("Better bring a scarf.")
        # if temperature < 10:
        #     print("Wear a very heavy coat")
        #     if temperature < 5:
        #         print("Use some handwarmers")
        #         if temperature < 0:
        #             print("Why dont we just stay inside")
# Nested elif
temperature = 16
if temperature < 25:
    print("its a bit chilly")
    if temperature < 15:
        print("Better bring a scarf")
    elif temperature < 18:
        print("Wear some ear muffs")
    elif temperature < 20:
        print("wear some nice gloves")
    
elif temperature < 35:
    print("Wear a jacket")
elif temperature < 45:
    print("We could probably wear some shorts today!")
else:
    print("Eh its relatively warm out today")

if temperature < 15:
    print("its super chilly")
elif temperature < 25:
    print("its pretty chilly")
# checking age restrictions

age = 121
if age >= 18:
    if age >= 21:
        print("You can drive, vote, and drink.....and smoke")
    else: #between 18 and 21
        print("You can drive and vote!")
else:
    print("You're too young to drive or vote.")

# weekend activities
day = "Saturday"
time = "evening"
if day == "Saturday":
    if time == "Morning":
        print("Jogging and then watching cartoons")
    elif time == "afternoon":
        print("Get some wings with lemon pepper after lifting some weights")
    elif time == "evening":
        print("Anthony is doing some yoga and then drink some beer")
    else:
        print("Ya know, just having a good time")

    
genre = "Fantasy"
author = "JRR Tolkien"

if genre == "Fantasy":
    if author == "J.K. Rowling":
        print("Oh cool, Harry Potter!")
    elif author == "JRR Tolkien":
        print("OH VERY COOL, Lord of the Rings.")
    else:
        print("Thats a book by another and its fantasy so probaly Brian Sanderson")


# super nested ifs, where each if elif will have its own nest
fruit = "Banana"
is_ripe = True
has_spots = False

if fruit == "Apple":
    if is_ripe and not has_spots:
        print("Oh baby, a percet apple!")
    elif not is_ripe and not has_spots:
        print("Let it ripen a bit more.")
    else:
        print("This is a great apple for an Apple Pie")
elif fruit == "Banana":
    if is_ripe and not has_spots:
        print("This banana is ready to eat! Save the peel for Mario Kart")
    elif not is_ripe:
        print("This banana is green!")
    else:
        print("This is a perfect banan for banana bread")


# checking some movie release dates
movie = "Hot Rod"
release_year = 2007
duration_minutes = 90

if movie == "Inception":
    # checking if the release_year is between 2000 and 2020 and duration is over 120 minutes
    if 2000 <= release_year <= 2020 and duration_minutes > 120:
        print("A Modern classic with a runtime of over 2 hours")
    elif release_year < 2000:
        print("A gem from the past")
    else:
        print("A recent masterpiece")
elif movie == "Lord of the Rings: The Two Towers":
    if 2000 <= release_year <= 2020 and duration_minutes > 180:
        print("An absolutely wonderful film, that is really long and while it was cool in the theater. Those chairs are not ver ycomfy.")
    elif release_year < 2000:
        print("A pretty cool classic movie")
    else:
        print("A very recent banger of a film. ")
else:
    print("Im sure thats also a great movie.")



# SHORTHAND CONDITIONAL - Ternary
# shorthand is best used when the conditions and the outcomes can be expressed on a single line  
# x = 5, y = 10
x, y = 5, 10
# what is being executed | if this condition |else do this
print("x is greater") if x > y else print("y is greater")

# set a variable with the shorthand
weather = "sunny"
activity = "beach" if weather == "sunny" else "video games"
print(activity)

# using a range within the shorthand -> with parentheses
hour_of_day = 1 # using an integer to represent the hour in 24 hour format
energy_level = 3 #possibly over 9000

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level < 4 else "tea"
print(beverage)

# PASS - allows us to skip over a block of code and come back to it later
# defining functions but arent entirely what you want that function to do yet
# you can apply the pass to conditionals, functions, loops
if beverage == "coffee":
    pass
    
elif beverage == "tea":
    print("Enjoy your tea with some nice crumpets")




