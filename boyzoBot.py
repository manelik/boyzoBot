import twitter
import time
import random

boyzoBot= twitter.Api()

boyzoBot.SetCredentials(username='boyzoBot',password='rantrant')

#boyzoBot.PostUpdate('ranteando desde python porque no me entendi con las librerias para C++')

mood = 10

while (mood>0):
  N = random.random()*4
  boyzoBot.PostUpdate('Rant '+'rant'*int(N)),
  time.sleep(random.gauss(mu=30,sigma=8)),
  mood -= 1


boyzoBot.PostUpdate('Ya me canse, ranteare manana')

boyzoBot.ClearCredentials()
