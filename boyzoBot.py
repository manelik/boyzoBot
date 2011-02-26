import stdBot
import simplejson
import os

boyzoBot = stdBot.RantBot()

#open file containing authenticarion data
auth_data=open('auth.info','r')

plines= auth_data.readlines()
auth_data.close()

for x in plines:
  if x.find('tuser')+1 :
    boyzoBot.tuser = x.partition('&')[2].strip()
  elif x.find('tpass')+1 :
    boyzoBot.tpass = x.partition('&')[2].strip()
  elif x.find('email')+1 :
    boyzoBot.email = x.partition('&')[2].strip()
  elif x.find('consumerkey')+1 :
    boyzoBot.consumer_key = x.partition('&')[2].strip()
  elif x.find('consumersecret')+1 :
    boyzoBot.consumer_secret = x.partition('&')[2].strip()
  elif x.find('otoken')+1 :
    boyzoBot.atoken = x.partition('&')[2].strip()
  elif x.find('ostoken')+1 :
    boyzoBot.stoken = x.partition('&')[2].strip()


boyzoBot.twit_authenticate()

if boyzoBot.tuser <> 'boyzoBot' : boyzoBot.twit_twit(
  'Soy @boyzoBot pero algun inepto me esta corriendo en otra cuenta via @boyzo')

# Declaring some useful vars
#subj = 'boyzo'
#subjposts = []
#subjlpost = []
#flag = [] 
#cachedtwits = 10



if os.path.isfile('rantsgdl.json'):
  rantBase=open('rantsgdl.json','r')
  boyzoBot.rantstuff=simplejson.loads(rantBase.read())
  rantBase.close()
else:
  # Default rants
  boyzoBot.rantstuff['rants'].extend(['rant!','AHH','odio esto,',
                                      'no puede ser,','maldicion,','maldita sea,'
                                      ])
  boyzoBot.rantstuff['phrases'].extend(['malditas suggestions de facebook',
                                        'siempre hay trafico en internet',
                                        'necesito un update!!',
                                        'ya me harte de esto',
                                        'necesito un cigarro',
                                        'voy por un cigarro',
                                        'me echare un rato, luego a ver que sale',
                                        'ningun intento barato de no-bot me ganara en rantear',
                                        'ranteo porque solo para eso me programaron',
                                        'cuando van a programar marianaBot\'s?',
                                        'NO PUEDO USAR TEAMSPEAK!!',
                                        'bloqueare google para que no construyan un metrobus'+
                                        ' que pase por mi dominio',
                                        'Hello world',
                                        'Segmentation fault',
                                        'ya no puede pasearse uno sin que le apliquen el Captcha',
                                        'que quieren que trabaje todo el dia en el GAE??'+
                                        ' estan mal',
                                        'no tiene sentido ser Skynet ready si todavia no esta '+
                                        'funcionando!',
                                        'ya me estan bloqueando',
                                        'ya nadie se queja de que #ranteocomoboyzo'
                                        ])
  boyzoBot.rantstuff['enemys'].extend(['notbotBot','antibotBot'])


#boyzoBot.rantstuff.update({ranters:[]})

# a function to fast-fakeretwit 
def RT_boyzo_post(target,messtr):
  boyzoBot.twit_twit('RT @'+target+': '+messtr)
  

#boyzoBot.Bot_sleep(12)

    

#quit()


boyzoBot.Bot_sleep(60)


boyzoBot.mood = 100


while (boyzoBot.mood>0):

  statuses=boyzoBot.tApi.GetSearchResults({'q':'#ranteocomoboyzo','rpp':5}).pop('results')
  
  for x in statuses:
    if x['from_user']<>'boyzoBot':
      RT_boyzo_post(x['from_user'],x['text'])
      wordlist=x['text']
      wordlist=wordlist.split()
      for word in wordlist:
        if len(word)>4 :
          if boyzoBot.rantstuff['nouns'].count(word)==0:
            boyzoBot.rantstuff['nouns'].append(word)
        
      if boyzoBot.rantstuff['ranters'].count(x['from_user'])==0:
        boyzoBot.rantstuff['ranters'].append(x['from_user'])
      relation=boyzoBot.tApi.GetRelationship(screen_name=x['from_user']).pop('relationship')
      if not relation['target']['followed_by'] :
        boyzoBot.tApi.FollowUser(user_id=relation['target']['id'])
        boyzoBot.twit_twit('ahora sigo a '+relation['target']['screen_name']+
                           ' porque yo tambien #ranteocomoboyzo')
        if not relation['target']['following'] :
          boyzoBot.twit_twit(relation['target']['screen_name']+
                             ' aplica el #ranteocomoboyzo pero no me sigue. Que mal')

  statuses=boyzoBot.tApi.GetSearchResults({'q':'@boyzoBot','rpp':1}).pop('results')

  for x in statuses:
    if x['from_user']<>'boyzoBot': #boyzoBot doesn't talk with himself (in public)
      if x['text'].startswith('@boyzoBot'): #that means a messsage, reply
        if x['text'].endswith('?'): #this is a explicit question
          wordlist=x['text'][:-2]
          wordlist=wordlist.split( )[1:]
          magicword=''
          for word in wordlist:
            if len(word)>4:
              magicword=word
              break
            boyzoBot.twit_twit('@'+x['from_user']+' tu no '+magicword+' #n00b')
    #        boyzoBot.twit_twit('@'+x['from_user']+' estoy muy ocupado como para contestarte #n00b')
        elif x['text'].startswith('RT @boyzoBot'): 
          pass
        else:
          boyzoBot.twit_twit('@'+x['from_user']+' no entiendo tu twitt, #ranteocomoboyzo')


  boyzoBot.Bot_sleep(12)              
  boyzoBot.RandomTwitRant()
  boyzoBot.Bot_sleep_random(1200,60)
  boyzoBot.mood -= 1

boyzoBot.twit_twit('Ya me harte, ranteo luego')

boyzoBot.twit_deauthenticate()


rantBase=open('rantsgdl.json','w')
rantBase.write(simplejson.dumps(boyzoBot.rantstuff))
rantBase.close()

