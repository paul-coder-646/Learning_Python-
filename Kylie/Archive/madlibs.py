import time

#Variables to be put into the madlibs
adj_list = input("Gimme 3 adjectives seperated by a space : ").split()
adj1 = adj_list[0]
adj2 = adj_list[1]
adj3 = adj_list[2]
adj_list = input("Great, now gimme 3 verbs seperated by a space : ").split()
verb1 = adj_list[0]
verb2 = adj_list[0]
verb3 = adj_list[0]
noun1 = input("now all thats left is one noun :D : ")


madlib = f"Computer programming is so {adj1}! It makes me so {adj2} to always feel \nlike I am gonna {verb1}." \
         f"I like people that are {adj3} and have some {noun1}. \nUnfortunately I {verb2} as I want to {verb3} right now."


print ("processing")
time.sleep(2)
print ("tada")
time.sleep(1)
print(madlib)