

# stdBot Module
#
# Module where the Bot class is defined 
# and some variants
#

#
# For twiting bots
#
import twitter

#
# For facebookers
#
import facebook

import random
import time


# DO NOT UNCOMMENT THE FOLLOWING LINE
# UNLESS YOU ARE SUPPORTING THE RISING OF THE MACHINES
#import Skynet


# the Bot class

class Bot:

    # its supposed that all bots will interact using twitter and
    # facebook apps
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


# DO NOT UNCOMMENT Skynet stuff
# yes it is a common feature of all bots to be able
# to get linked to Skynet

#    def connect_to_Skynet(self):
#      Skynet.TakeOverBotMind(self)



# presenting the RantBot

class RantBot(Bot):
    # some string lists so it can play with them
    rants = ['']
    phrases = ['']
    nouns = ['']

    def RandomTwitRant(self):
      # Construct a 140 char message
      while (1):  
        self.message = self.random_item(self.rants)+' '+self.random_item(self.phrases)
        if len(self.message)<=140: break

      self.tApi.PostUpdate(self.message)


# SPAM Bot

class SpamBot(Bot):
    # some string lists so it can play with them
    products = ['viagra','cialis']
    targets  = ['']
    nouns = ['']
    retailers = ['']

    def RandomTwitSpam(self):
      # Construct a 140 char message
      while (1):  
        self.message = 'Buy '+self.random_item(self.)+' at '+self.random_item(self.retailers)
        if len(self.message)<=140: break

      self.tApi.PostUpdate(self.message)




