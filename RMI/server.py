import Pyro4
import random

@Pyro4.expose
class RandomvalueGenerator(object): #randomvaluegenerator
    def get_fortune(self, name):
        return "Hello, {0}. Here is your Random Number.".format(name)        

@Pyro4.expose
class randomvalue(object):  #randomvalue
    def findrandom(self,a,b): # findRandom #find sum
        return random.randint(a,b)
  
# make a Pyro daemon
daemon = Pyro4.Daemon()
# find the name server
ns = Pyro4.locateNS()
# register the greeting maker as a Pyro object
uri= daemon.register(RandomvalueGenerator)
uri2=daemon.register(randomvalue)
# register the object with a name in the name server
ns.register("example.greeting", uri)
ns.register("example.Random_Number", uri2)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
