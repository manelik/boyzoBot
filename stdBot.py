
###################################
# stdBot Module
###################################

# Module where the Bot class is defined 
# and some variants
#

#
# For twiting bots
#
# All the authentication is now done with oauth
from oauth import oauth
from oauthtwitter import OAuthApi
#import pprint
#import os
#
# For facebookers
#
#import facebook

import random
import time

# Gravatar stuff yet to be implemented
# Check http://en.gravatar.com/site/implement/python
# import urllib, hashlib

# skynetready
try:
  import skynet
except ImportError:
  print 'Skynet still unavailable'


# the Bot class

class Bot:

    # its supposed that all bots will interact using twitter and
    # facebook apps
    mood = 10.0  # mood affects the behaviour
    tuser = ''   # twitter username
    tpass = ''   # twitter password
    consumer_key  = ''
    consumer_secret = ''
    atoken = ''
    stoken = ''

    tApi = OAuthApi(consumer_key,consumer_secret) # Api

    email = ''   # respectable bots have a valid email
                 # Should be a service providing an API
    emailpass = ''

    message = '' # for messages construction

    def random_item(self,token):
        """Picks a random item from a list.        
        """
        return token[int(random.random()*len(token))]

    def twit_authenticate(self):
        """Begin a twitter session.
        """
        self.tApi= OAuthApi(self.consumer_key, self.consumer_secret, self.atoken, self.stoken)
    
    def twit_deauthenticate(self):#deprecated
        #self.tApi.ClearCredentials()
        """Deprecated. 
        Left for compatibility with older versions.
        """
        pass
    def twit_twit(self,token):
        """Post a new status.
        """
        self.tApi.UpdateStatus(token[0:140])
    
    def twit_get_user_updates(self,usrname,num):
        """Get the last updates from a specific user.
        """
        return self.tApi.GetUserTimeline(user=usrname,count=num)
    
    def Bot_sleep_random(self,ctime,sigtime):
        """ Sleep a randomized amount of time.
        """
        time.sleep(random.gauss(mu=ctime,sigma=sigtime))
    
    def Bot_sleep(self,token):
        """ Sleep a fixed amount of time
        """
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
    enemys = ['']

    def RandomTwitRant(self):
        """Generate a random rant and post it.
        """
        # Construct a 140 char message
        while (1):  
            self.message = self.random_item(self.rants)+' '+self.random_item(self.phrases)
            if len(self.message)<=140: 
                break
        self.tApi.UpdateStatus(self.message)

    def RandomFakeRTwit(self,target):
        """Generate a random fake retweet
        """
        # Construct a 140 char message
        while (1):  
            self.message = ('RT @'+target+': '+self.random_item(self.rants)+
                            ' '+self.random_item(self.phrases))
            if len(self.message)<=140: 
                break
        self.tApi.UpdateStatus(self.message)


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
      self.tApi.UpdateStatus(self.message)

    def RandomDirectTwitSpam(self,target):
      # Construct a 140 char message
        while (1):  
            self.message = ('@'+target+'  Buy '+self.random_item(self.product)
                            +' at '+self.random_item(self.retailers))
            if len(self.message)<=140: break
            
        self.tApi.UpdateStatus(self.message)

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
    
