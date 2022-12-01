import Pyro4


# from RMI_Application.server import randomvalue

name = input("What is your name? ").strip()

# use name server object lookup uri shortcut
RandomvalueGenerator = Pyro4.Proxy("PYRONAME:example.greeting")
randomvalue =Pyro4.Proxy("PYRONAME:example.Random_Number")

print(randomvalue.findrandom(3,15))
print(RandomvalueGenerator.get_fortune(name))
