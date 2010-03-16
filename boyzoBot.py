import stdBot

boyzoBot = RantBot()

boyzoBot.tuser = 'boyzoBot'
boyzoBot.tpass = ''

boyzoBot.twit_authenticate()

boyzoBot.rants = ['rant!','AHH','odio esto','no puede ser','maldicion','maldita sea']

boyzoBot.phrases = ['malditos sugest\'s de facebook',
                    'siempre hay trafico en internet',
                    'necesito un update!!'
                    ]

while (mood>0):
  N = random.random()*4
  boyzoBot.PostUpdate('Rant '+'rant '*int(N)),
  time.sleep(random.gauss(mu=500,sigma=8)),
  mood -= 1


boyzoBot.PostUpdate('Ya me canse, ranteare manana')

boyzoBot.ClearCredentials()
