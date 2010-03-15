import twitter
import time
import random

boyzoBot= twitter.Api()

boyzoBot.SetCredentials(username='boyzoBot',password='')

boyzoBot.PostUpdate('Maldita sea, no puedo acceder al TeamSpeak')

mood = 0

while (mood>0):
  N = random.random()*4
  boyzoBot.PostUpdate('Rant '+'rant '*int(N)),
  time.sleep(random.gauss(mu=500,sigma=8)),
  mood -= 1


boyzoBot.PostUpdate('Ya me canse, ranteare manana')

boyzoBot.ClearCredentials()
