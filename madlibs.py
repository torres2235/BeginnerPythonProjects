name = "Joshua Torres"

#different ways to concatenate string
print("My name is " + name)
print("My name is {}".format(name))
print(f"My name is {name}") #fstream format

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)