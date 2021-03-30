import discord
from os import getenv
from requests import get
from random import choice
from googletrans import LANGUAGES
from googletrans import Translator
#--------------------------------------

import aqua_comandos  
import uptime

#--------------------------------------

prefix='~'
bot = discord.Client()
translator = Translator()

comandos = {
    prefix+'ajuda': [aqua_comandos.ajuda, prefix+"ajuda    #lista os comandos"],
    prefix+'traduz': [aqua_comandos.traduz, prefix+'traduz [texto] [origem] [destino]    #traduz o [texto] da lingua de [origem] para linga de [destino].'],
    prefix+'linguas': [aqua_comandos.linguas, prefix+'linguas    #mostra as linguas para traducao'],

  }

@bot.event
async def on_ready():
  print('----- Bot Online! -----')
  print(f'We have logged in as {bot.user}')
  print('Bot Latency:', bot.latency)
  print('Guilds: ', end='\n')
  for g in bot.guilds:
    print(f'     "{g}"',end='\n')
  print('\n')
  await bot.change_presence(activity=discord.Game(name=prefix+"ajuda - para ver os comandos"))



#______________________________B O M  D I A____________________________________________________________
@bot.event
async def on_voice_state_update(member, before, after):
  ヤルカシャソル = '361301183249252355'
  おはよう = bot.get_channel(705294471377584188)
  if (str(after.channel) == 'VARZEA') and not str(before.channel) == 'VARZEA' and str(member.id) == ヤルカシャソル:
    await おはよう.send(f"{translator.translate('bom dia', dest=choice(list(LANGUAGES.keys()))).text} ヤルカシャ ソル")



#______________________________L I S T E N I N G  C H A T____________________________________________________________
@bot.event
async def on_message(message):
  lista_palavras = get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.split('\n')

  if message.author == bot.user:
    return None

  if message.content.startswith(tuple(comandos.keys())):
    try:
      await comandos[message.content.lower().split()[0]][0](message, comandos)
    except:
      await message.channel.send('*Algo deu errado*')

  if bot.user.mentioned_in(message):
    await message.channel.send('Estou pensando em... "'+choice(lista_palavras)+'"!')

  if message.content == 'aqua':
    await message.channel.send('アクアです')

  if message.content == 'oi':
    await message.channel.send("Olá" +' '+ message.author.name +' !')
  


#______________________________M A I N____________________________________________________________
def main():
  bot.run(getenv('discord_token'))


main()
