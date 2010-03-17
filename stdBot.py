
###################################
# stdBot Module
###################################

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

# Gravatar stuff yet to be implemented
# Check http://en.gravatar.com/site/implement/python
# import urllib, hashlib



# DO NOT UNCOMMENT THE FOLLOWING LINE
# UNLESS YOU ARE SUPPORTING THE RISE OF THE MACHINES
#import Skynet


# the Bot class

class Bot:

    # its supposed that all bots will interact using twitter and
    # facebook apps
    mood = 10.0  # mood affects the behaviour
    tuser = ''   # twitter username
    tpass = ''   # twitter password
    tApi = twitter.Api() # Api

    email = ''   # respectable bots have a valid email
                 # Should be a service providing an API
    emailpass = ''

    message = '' # for messages construction

    def random_item(self,token):
        # Picks a random item from a list
        # token -list
        return token[int(random.random()*len(token))]

    def twit_authenticate(self):
        self.tApi.SetCredentials(username=self.tuser,password=self.tpass)
    
    def twit_deauthenticate(self):
        self.tApi.ClearCredentials()
    
    def twit_twit(self,token):
        self.tApi.PostUpdate(token[0:140])
    
    def twit_get_user_updates(self,usrname,num):
        return self.tApi.GetUserTimeline(user=usrname,count=num)
    
    def Bot_sleep_random(self,ctime,sigtime):
        time.sleep(random.gauss(mu=ctime,sigma=sigtime))
    
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
            if len(self.message)<=140: 
                break
        self.tApi.PostUpdate(self.message)

    def RandomFakeRTwit(self,target):
        # Construct a 140 char message
        while (1):  
            self.message = ('RT @'+target+': '+self.random_item(self.rants)+
                            ' '+self.random_item(self.phrases))
            if len(self.message)<=140: 
                break
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
          self.message = 'Buy '+self.random_item(self.product)+' at '+self.random_item(self.retailers)
          if len(self.message)<=140: 
              break
      self.tApi.PostUpdate(self.message)

    def RandomDirectTwitSpam(self,target):
      # Construct a 140 char message
        while (1):  
            self.message = ('@'+target+'  Buy '+self.random_item(self.product)
                            +' at '+self.random_item(self.retailers))
            if len(self.message)<=140: break
            
        self.tApi.PostUpdate(self.message)

#
# MegaBot
#
# A bot that gets the abilities of those who defeats
# NO RECURSION PLEASE!!

class MegaBot(Bot):
    beatenBots = []    # a list of beatenBots
    maxHP = 100.0       
    currHp= 100.0

    def TakePowers(self,beatBot):
        self.beatenBots.append(beatBot)
    
