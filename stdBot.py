

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

    def random_item(self,token):
      return token[int(random.random()*len(token))]

    def twit_authenticate(self):
      self.tApi.SetCredentials(username=self.tuser,password=self.tpass)

    def twit_deauthenticate(self):
      self.tApi.ClearCredentials()

    def twit_twit(self,token):
      self.tApi.PostUpdate(token)

    def Bot_sleep_random(self):
      time.sleep(random.gauss(mu=500,sigma=100))

    def Bot_sleep(self,token):
      time.sleep(token) # token in seconds
    

# presenting the RantBot

class RantBot(Bot):
    # some string lists so it can play with them
    rants = ['']
    phrases = ['']
    nouns = ['']

    def RandomTwitRant(self):
      # Construct a 140 char message
      while (1):  
        self.message = self.random_item(self.rants)+''+self.random_item(self.phrases)
        if len(self.message)<=140:
            break

      self.tApi.PostUpdate(self.message)



