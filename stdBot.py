

# stdBot Module
#
# Module where the Bot class is defined 
#
#

#
# For twiting bots
#

import twitter
import random
import time


# the Bot class

class Bot:
    mood = 10.0  # mood affects the behaviour
    tuser = ''   # twitter username
    tpass = ''   # twitter password
    tApi = twitter.Api() # Api
    message = '' # for messages construction

    def random_item(token):
      return token[int(random.random()*len(token))]

    def twit_authenticate():
      tApi.SetCredentials(username=tuser,password=tpass)

    def Bot_sleep_random():
      time.sleep(random.gauss(mu=500,sigma=100))

    def Bot_sleep(token):
      time.sleep(token) # token in seconds
    

# presenting the RantBot

class RantBot(Bot):
    # some string lists so it can play with them
    rants = ['']
    phrases = ['']
    nouns = ['']

    def RandomTwitRant():
      # Construct a 140 char message
      while (1):  
        message = random_item(rants)+''+random_item(phrases)
        if len(message)<=140:
            break

      tApi.PostUpdate(message)



