Guest_list ={
    "Randy": "Germany",
    "Karla": "France",
    "Nadeem":"USA"
}
def G_list(name):
    done = ""
    f = ""
    place = ""
    found = False
    for key,val in Guest_list.items():
        if  key == name:
            f = key
            place = val
            found = True


    if found == True:
        print("Hi! I'm a guest.")
        print()
    else:
        print("Hi! I'm {}, and I'm from {}.".format(f,place))
        print()
        print("Hello",f, "It's nice to have you back how is",place)
        # Hi! I'm Randy, and I'm from Germany.
        #"Hello, {}. You are {}.".format(name, age)
        #"Hello",f, "It's nice to have you back how is",place,"?"
#print("Hello please enter your name: ")
#text = input()
#G_list(text)
G_list("Gus")
G_list("Nadeem")
G_list("David")
