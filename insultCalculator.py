import random

print(random.randrange(0, 4))
print(random.randrange(0, 4))
print(random.randrange(0, 4))

groceries = ["apples", "bread", "eggs", "cake"]

randNum = random.randrange(0, 4)

#output a random item from groceries list
#This syntax works, I had to create a variable to store
#a random number generator, it wouldn't work if I just
#tried to put the entire module in the brackets

print(groceries[randNum])

#Try constructing a sentence with
#a random word
groceryItemVar = "I think I will have a "
print(groceryItemVar + groceries[randNum])

#The above code worked, now try to see if you can use more]
#than one of the random words

longerItemVar = "I would like some %s and some %s "

print(longerItemVar % (groceries[randNum], groceries[randNum]))

#The above code worked but kept applying the same index number
#to both of the grocery list items integrated into the sentence

#code should ask user, would you like to receive a compliment
#Insult Generator
#Sample sentence:
#You (adjective) (noun). I bet your (noun) (verb) your (noun) !
#You (dirty) (lowlife). I bet your (mom) (licks) your (butt) !


#declarations
adjectiveInsult = ["smelly", "dirty", "crude", "kniving", "simple", "filthy", "slimy"]
noun = ["lowlife", "simpleton", "knave", "drooly", "gremlin", "monster", "shlub"]
famNoun = ["mom", "brother", "dad", "sister", "uncle", "grandma", "grandpa"]
verb = ["licks", "kicks", "smells", "rubs", "hits", "busts", "kisses"]
bodyPart = ["butt", "leg", "elbow", "belly", "knuckles", "cheeks", "shoulder"]
randIndexNum = random.randrange(0, 7)

try:
    insultSentence = "You %s %s. I bet your %s %s your %s!"
    print(insultSentence % (adjectiveInsult[randIndexNum], noun[randIndexNum], famNoun[randIndexNum], verb[randIndexNum], bodyPart[randIndexNum]))  
except Exception as e:
    print("There was an error")
    print(e)
finally:
    print("Done")


insultSentence = "You %s %s. I bet your %s %s your %s!"
print(insultSentence % (adjectiveInsult[randIndexNum], noun[randIndexNum], famNoun[randIndexNum], verb[randIndexNum], bodyPart[randIndexNum]))


#for x in range(10):
    #print random.randint(1, 101)
    ##The code will print 10 random values of numbers between 1 and 100.
    #The second line, for x in range(10), determines how many values will be printed


#print groceries(random.randit(1, 101))

#print(groceries(randint))



##height = 20000

#if height < 10000:
 #   print("That's too short")

#elif height > 20000:
#    print("That's too high")

#elif height < 5000:
 #   print("That's way too short")

#else: 
 #   print("That's just right")
    
#for x in range(0, 5):
 #   print("bananas")

#cups = 10
#lemonaide = 7

#while cups < 50 or lemonaide < 10:
 #   print("We need another cup")
   # cups = cups + 1
   # lemonaide = lemonaide +1
    
#x = 5
#y = 10

#while x < 10 or y < 20:
 #   print(":)")
  #  x = x + 1
   # y = y + 1
#rain = True
#dryWeather = False

#while rain == True:
 #   print("get an umberlla")
  #  rain = False

#print("Welcome to Spaghetto's, I'm your host, Spaghetti Eddie!")
#print("Please select an option from the menu below")

#print("Press 1 for homestlye spaghetti $5.00")
#print("Press 2 for spaghetti bolongese $5.50")
#print("Press 3 for cheese ravioli $6.00")
#print("Press 4 for zuccini pasta $4.00")
#print("Press 5 for garlic bread and marinara sauce $6.50")
#print("Press 0 to get your total or quit")

#userNum = int(input())
#totalCost = 0

#while userNum >= 0:
#    if userNum == 1:
#        print("You have selected homstyle spaghetti EMPTY ")
#        totalCost = totalCost + 5.0
#we will start at casting the integer to the string
