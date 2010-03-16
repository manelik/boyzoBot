import stdBot

boyzoBot = stdBot.RantBot()

boyzoBot.tuser = 'boyzoBot'
boyzoBot.tpass = ''

boyzoBot.twit_authenticate()

if boyzoBot.tuser <> 'boyzoBot' : boyzoBot.twit_twit(
'Soy @boyzoBot pero algun inepto me esta corriendo en otra cuenta via @boyzo')


#Just for testing
boyzoBot.rants.extend(['rant!','AHH','odio esto,',
                        'no puede ser,,','maldicion,','maldita sea,'
                       ])

boyzoBot.phrases.extend(['malditas suggestions de facebook',
                         'siempre hay trafico en internet',
                         'necesito un update!!'
                         'ya me harte de esto',
                         'necesito un cigarro',
                         'voy por un cigarro',
                         'me echare un rato, luego a ver que sale',
                         'ningun intento barato de no-bot me ganara en rantear',
                         'ranteo porque solo para eso me programaron',
                         'cuando van a programar marianaBot\'s?',
                         'NO PUEDO USAR TEAMSPEAK!!',
                         'bloqueare google para que no construyan un metrobus'+
                         ' que pase por mi dominio'
                         ])

while (boyzoBot.mood>0):
  boyzoBot.RandomTwitRant()
  boyzoBot.Bot_sleep_random()
  boyzoBot.mood -= 1


boyzoBot.twit_twit('Ya me harte de este testrun!')

boyzoBot.twit_deauthenticate()
