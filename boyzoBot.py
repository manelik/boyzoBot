import stdBot

boyzoBot = stdBot.RantBot()

#open file containing authenticarion data
auth_data=open('auth.info','r')

plines= auth_data.readlines()
auth_data.close()

for x in plines:
  if x.find('tuser')+1 :
    boyzoBot.tuser = x.partition('&')[2]
  elif x.find('')+1 :
    boyzoBot.tpass = x.partition('&')[2]
  elif x.find('')+1 :
    boyzoBot.email = x.partition('&')[2]
  elif x.find('consumerkey')+1 :
    boyzoBot.consumer_key = x.partition('&')[2]
  elif x.find('consumersecret')+1 :
    boyzoBot.consumer_secret = x.partition('&')[2]
  elif x.find('otoken')+1 :
    boyzoBot.atoken = x.partition('&')[2]
  elif x.find('ostoken')+1 :
    boyzoBot.stoken = x.partition('&')[2]


boyzoBot.twit_authenticate()

if boyzoBot.tuser <> 'boyzoBot' : boyzoBot.twit_twit(
  'Soy @boyzoBot pero algun inepto me esta corriendo en otra cuenta via @boyzo')

# Declaring some useful vars
subj = 'boyzo'
subjposts = []
subjlpost = []
flag = [] 
cachedtwits = 10


boyzoBot.rants.extend(['rant!','AHH','odio esto,',
                        'no puede ser,','maldicion,','maldita sea,'
                       ])

boyzoBot.phrases.extend(['malditas suggestions de facebook',
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
                         'funcionando!'
                         'ya me estan bloqueando'
                         ])

boyzoBot.enemys.extend(['notbotBot','antibotBot'])

# a function to fast-fakeretwit 
def RT_boyzo_post(target,messtr):
  boyzoBot.twit_twit('RT @'+target+': '+messtr)
  
#subjposts = boyzoBot.twit_get_user_updates(subj,cachedtwits)#
#subjlpost = boyzoBot.twit_get_user_updates(subj,1)
#subjlpost[0] = subjposts[len(subjposts)/2]

#RT_boyzo_post(subj,subjlpost[0].text)


#boyzoBot.Bot_sleep(12)
boyzoBot.twit_twit('YO NI QUERIA IR AL APICAMP!!')

boyzoBot.Bot_sleep(12)
#boyzoBot.mood = 100
while (boyzoBot.mood>0):
#  subjposts = boyzoBot.twit_get_user_updates(subj,cachedtwits)
#  if subjposts.count(subjlpost[0]):
#    if subjposts.index(subjlpost[0]):
#      for i in range( len(subjposts), subjposts.index(subjlpost[0]), -1):
#        subjposts.pop(i-1)
#        if not len(subjposts): subjlpost[0]=subjposts[0]
#        subjposts.reverse()
#        for s in subjposts:
#          RT_boyzo_post(subj,s.text)
#          boyzoBot.Bot_sleep(5)
#  else:
#    boyzoBot.twit_twit('@'+subj+' tuiteas demasiado, ya no hallo tu ultimo twit,'+
#                       ' extendiendo el cache')
#    boyzoBot.sleep(5)
#    if cachedtwits < 100 : 
#      cachedtwits += 10
#    else:
#      boyzoBot.twit_twit('@'+subj+' felicidades has tuiteado mas de lo que me es '+
#                         'permitido trackear')
#    subjlpost = []
#    subjlpost = boyzoBot.twit_get_user_updates(subj,1)
#    RT_boyzo_post(subj,subjlpost[0].text)
#    print subjlpost[0].text

  boyzoBot.Bot_sleep(12)              
  boyzoBot.RandomTwitRant()
  boyzoBot.Bot_sleep_random(1200,60)
  boyzoBot.mood -= 1

boyzoBot.twit_twit('Ya me harte, ranteo luego')

boyzoBot.twit_deauthenticate()
