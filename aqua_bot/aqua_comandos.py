from googletrans import LANGUAGES
from googletrans import Translator

translator = Translator()



async def ajuda(message, comandos :dict):
  msg = "```\n"
  for c in comandos.keys():
    msg += comandos[c][1]+'\n'
  msg += "```"
  await message.channel.send(msg)



async def traduz(message, _):
  msg = message.content.strip().lower().split()
  
  if len(msg)<4:
    return Exception

  cod1 = msg[-1]
  cod2 = msg[-2]

  if (len(cod1) > 2 and cod1 in list(LANGUAGES.values())):
    for k in LANGUAGES.keys():
      if LANGUAGES[k] == cod1:
        cod1 = k
  elif (len(cod1) == 2 and cod1 not in list(LANGUAGES.keys())):
    return Exception
  
  if (len(cod2) > 2 and cod2 in list(LANGUAGES.values())):
    for k in LANGUAGES.keys():
      if LANGUAGES[k] == cod2:
        cod2 = k
  elif (len(cod2) == 2 and cod2 not in list(LANGUAGES.keys())):
    return Exception
  
  msg = ' '.join(msg[1:-2])
  out = translator.translate(text=msg, dest=cod1, src=cod2).text
  await message.channel.send(out)



async def linguas(message, _):
  msg = "```\n"
  for k in LANGUAGES.keys():
    msg += str(k)+' - '+str(LANGUAGES[k])+'\n'
  msg += "```"
  await message.channel.send(msg)
