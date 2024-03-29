import discord
import asyncio
from discord.ext import commands
from discord.ext.commands   import bot

# token = input("Input your Discord Bot's token.\n")
token = 'NzUwNjk3NjkyNjMxNTMxNTMw.X0-TtQ.LDzx90AHZTX-AEji5Qt3HfeYE78'
# ITG
amongVoiceChannel = 750634010723614741
amongTextChannel = 750634259483590706
fantasmikosChannel = 750691724589793291
codeChannel = 750700369901912124
fiotChannel = 690522033955799051
ticChannel = 690523256083578931
cmpdChannel = 747716139357831259
rChannel = 688865859246358549

client = commands.Bot(command_prefix = "!")

client.remove_command("help")


# Starts the bot, with a status.
@client.event
async def on_ready():
    print('Among Us Bot is online!')
    await client.change_presence(status = discord.Status.online, activity=discord.Game('among us'))


# Error handling.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Missing Requirement Error [DB10]", description="Pass in all required arguments.", colour=discord.Color.blue())
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Missing Permissions Error [DB11]", description="You are not able to use this command because you do not have the required permissions.", colour=discord.Color.blue())
        await ctx.send(embed=embed)


# Ping command, gives latency of the bot to the user.
@client.command()
async def ping(ctx):
    print("ping " + str(ctx.author) + " en " + str(ctx.channel))
    embed = discord.Embed(title="Pong!", description=":ping_pong:", colour=discord.Color.blue())
    embed.add_field(name="The latency for Among Us Bot is...", value=f"{round(client.latency * 1000)} ms")
    await ctx.send(embed=embed)

@client.command(aliases=['un'])
async def unete(ctx):
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
@client.command(aliases=['ve'])
async def vete(ctx):
    await ctx.voice_client.disconnect()
    
# Mute all players.
@client.command(aliases=['mute','m'])
async def mutePlayers(ctx):
    print("mute " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    fixed_channel = client.get_channel(ctx.channel.id)
    members = fixed_channel.members #finds members connected to the channel
    await ctx.send('Shhhh :shushing_face:')
    # await ctx.send('Montero callate la puta boca :shushing_face:')
    for member in members:
        await member.edit(mute=True, deafen=False)
    for member in members:
        for role in member.roles:
            if role.name == "Musica":
                await member.edit(mute=False, deafen=True)

# Unmute all players.
@client.command(aliases=['unmute','u'])
async def unmutePlayers(ctx):
    print("unmute " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    among_channel = client.get_channel(ctx.channel.id)
    among_members = among_channel.members #finds members connected to the channel
    fantasmikos_channel = client.get_channel(fantasmikosChannel)
    fantasmikos_members = fantasmikos_channel.members #finds members connected to the channel
    for member in fantasmikos_members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)
    await ctx.send('A discutir :thinking:')
    for member in among_members:
        await member.edit(mute=False, deafen=False)
    for member in among_members:
        for role in member.roles:
            if role.name == "Musica":
                await member.edit(mute=True, deafen=True)

# Unmute all players.
@client.command(aliases=['fiot', 'f'])
async def fiotMeeting(ctx):
    print("fiot " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(fiotChannel)
    for userRole in ctx.author.roles:
        if userRole.name == "FIOT":
            for member in ctx.guild.members:
                for role in member.roles:
                    if role.name == "FIOT":
                        await member.edit(mute=False, deafen=False, voice_channel=among_channel)
        else:
            await ctx.author.edit(mute=False, deafen=False, voice_channel=among_channel)

# Unmute all players.
@client.command(aliases=['desfiot', 'ufiot', 'uf'])
async def desfiotMeeting(ctx):
    print("desfiot " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(ticChannel)
    fantasmikos_channel = client.get_channel(fiotChannel)
    fantasmikos_members = fantasmikos_channel.members #finds members connected to the channel
    for member in fantasmikos_members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)


# Unmute all players.
@client.command(aliases=['cmpd', 'C'])
async def cmpdMeeting(ctx):
    print("cmpd " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(cmpdChannel)
    for userRole in ctx.author.roles:
        if userRole.name == "CMPD":
            for member in ctx.guild.members:
                for role in member.roles:
                    if role.name == "CMPD":
                        await member.edit(mute=False, deafen=False, voice_channel=among_channel)
        else:
            await ctx.author.edit(mute=False, deafen=False, voice_channel=among_channel)

# Unmute all players.
@client.command(aliases=['descmpd', 'ucmpd', 'uc'])
async def descmpdMeeting(ctx):
    print("descmpd " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(ticChannel)
    fantasmikos_channel = client.get_channel(cmpdChannel)
    fantasmikos_members = fantasmikos_channel.members #finds members connected to the channel
    for member in fantasmikos_members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)

# Unmute all players.
@client.command(aliases=['among'])
async def amongMeeting(ctx):
    print("among " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(amongVoiceChannel)
    for member in ctx.guild.members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)

# Unmute all players.
@client.command(aliases=['tic'])
async def ticMeeting(ctx):
    print("tic " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(ticChannel)
    for member in ctx.guild.members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)

@client.command(aliases=['baño', 'ivan'])
async def banoMeeting(ctx):
    print("1")
    tic_channel = client.get_channel(ticChannel)
    bano_channel = client.get_channel(banoChannel)
    miembros = []
    print("1.1")
    for member in ctx.guild.members:
        print("1.2")
        miembros.append(member)
        print("2")
        if member.id == 292802384705617920:
            me = member
    print(len(miembros))
    if len(miembros) > 0:
        miembros.shuffle()
        await miembros[0].edit(mute=False, deafen=False, voice_channel=bano_channel)
        await me.edit(mute=False, deafen=False, voice_channel=bano_channel)


# Starts the game.
@client.command(aliases=['musica'])
async def musicote(ctx):
    print("startgame " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(rChannel)
    await channel.send('!play https://open.spotify.com/playlist/0BgRKibZdo25bU7gqORAgi?si=loueRIqyS0WX7uTeWe6Haw')
    await channel.send('!shuffle')
        
# Starts the game.
@client.command(aliases=['start', 's'])
async def startgame(ctx):
    print("startgame " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"{ctx.author} está reclutando gente!", description="Haz click en el checkmark para marcar listo!", colour=discord.Color.blue())
    await ctx.send('Game Starting! @everyone')
    message = await ctx.send(embed=embed)
    emojis = '✅'
    for emoji in emojis:
        await message.add_reaction(emoji)

# Reaction events
@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    if user.bot:
        return
    if emoji == '✅':
        fixed_channel = client.get_channel(amongTextChannel) # General / main chat channel ID
        await fixed_channel.send(f'{user.mention} está listo para jugar! [{reaction.count - 1}/10]')
        # role = discord.utils.get(user.guild.roles, name="Amonger")
        # await user.add_roles(role)


@client.event
async def on_reaction_remove(reaction, user):
    emoji = reaction.emoji
    if user.bot:
        return
    if emoji == '✅':
        fixed_channel = client.get_channel(amongTextChannel) # General / main chat channel ID
        await fixed_channel.send(f'{user.mention} ya no va a jugar! [{reaction.count - 1}/10]')


# Code command, gives the code to code channel. Usage is !code {insert code here}
@client.command(aliases=['c'])
async def code(ctx):
    print("code " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='El código de la partida es:')
    embed.add_field(name='Code:', value=f"{ctx.message.content.replace('!code ', '').replace('!c ', '')}")
    await ctx.send(embed=embed)
    channel = client.get_channel(codeChannel) # Code channel.
    await channel.purge()
    await channel.send(embed=embed)

# set among channel
@client.command(aliases=['avc'])
async def avchannel(ctx):
    await ctx.channel.purge(limit=1)
    amongVoiceChannel = ctx.message.content.replace('!achannel ', '')

# set among channel
@client.command(aliases=['atc'])
async def atchannel(ctx):
    await ctx.channel.purge(limit=1)
    amongTextChannel = ctx.message.content.replace('!achannel ', '')

# set fantasmikos channel
@client.command(aliases=['fc'])
async def fchannel(ctx):
    await ctx.channel.purge(limit=1)
    fantasmikosChannel = ctx.message.content.replace('!fchannel ', '')

# set fantasmikos channel
@client.command(aliases=['cc'])
async def cchannel(ctx):
    await ctx.channel.purge(limit=1)
    amongVoiceChannel = ctx.message.content.replace('!cchannel ', '')

# Help command
@client.command(aliases=['commands','h'])
async def help(ctx):
    print("help " + str(ctx.author) + " en " + str(ctx.channel))
    channelName = client.get_channel(amongVoiceChannel)
    fiotName = client.get_channel(fiotChannel)
    cmpdName = client.get_channel(cmpdChannel)
    ticName = client.get_channel(ticChannel)

    embed = discord.Embed(title='Comandos de Among the Bot:', colour=discord.Color.blue())
    embed.add_field(name='Code (c) {code}', value='Envía al canal #code el código de la partida.\n')
    embed.add_field(name='startgame (s)', value='Comienza la partida y permite a los miembros estar listos.\n')
    embed.add_field(name='Mute (m)', value='Mutea y ensordece a los miembros del canal ' + str(channelName) + '.')
    embed.add_field(name='unMute (u)', value='Desmutea y desensordece a los miembros del canal ' + str(channelName) + '.')
    embed.add_field(name='Ping', value='Muestra la lantencia de bot con los servidores de discord.')
    embed.add_field(name='cancelgame (cancel)', value='Muestra un mensaje indicando que se ha cancelado la partida.')
    embed.add_field(name='FalseAlarm', value='Echarle la culpa a alguien por una falsa alarma.')
    embed.add_field(name='StartGameNoPing', value='Empezar el juego, pero sin avisar.')
    embed.add_field(name='ImposterWon', value='!imposterwon {imposters}. Shows who the imposters were, and when they won!')
    embed.add_field(name='CrewWon', value='!crewwon {imposters}. Shows that the crew won and who the imposters were.')
    embed.add_field(name='Among', value='Mueve a todos los miembros conectados al canal de voz ' + str(channelName) + '.')
    embed.add_field(name='HotKeys en el juego', value='Tab: ver el mapa \n Space, e: use')
    embed.add_field(name='fiot (f)', value='Mueve al equipo FIOT a ' + str(fiotName) + '.')
    embed.add_field(name='desfiot (uf, ufiot)', value='Mueve al equipo FIOT a ' + str(ticName) + '.')
    embed.add_field(name='cpmd (C)', value='Mueve al equipo CPMD a ' + str(cmpdName) + '.')
    embed.add_field(name='descmpd (uc, ucmpd)', value='Mueve al equipo CMPD a ' + str(ticName) + '.')
    await ctx.send(embed=embed)


# Cancel game command, just cancels a lobby.
@client.command(aliases=['cancel'])
async def cancelgame(ctx):
    print("cancel " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{ctx.author} ha cancelado la partida', description='A casita.')
    await ctx.send(embed=embed)
    channel = client.get_channel(codeChannel) # Code channel.
    await channel.purge()


# False Alarm command, puts a message in the code channel, and in the main chat that it was a false alarm.
@client.command()
async def falsealarm(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='False Alarm.', description=f'Blame {ctx.message.content.replace("!falsealarm ", "")}')
    channel = client.get_channel(codeChannel) # Code channel.
    # await channel.purge(limit=2)
    # await channel.send(embed=embed)
    await ctx.send(embed=embed)

# Borra el canal among us
@client.command()
async def clear(ctx):
    print("clear " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='False Alarm.', description=f'Blame {ctx.message.content.replace("!falsealarm ", "")}')
    channel = client.get_channel(codeChannel) # Code channel.
    await channel.purge()
    await help(ctx)


# This is a copy paste of the start game, except without the @everyone ping.
@client.command(aliases=['noping', 'startnoping'])
async def startgamenoping(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"{ctx.author} is starting a lobby!", description="Click the checkmark to ready up!", colour=discord.Color.blue())
    await ctx.send('Game Starting!')
    message = await ctx.send(embed=embed)
    emojis = '✅'
    for emoji in emojis:
        await message.add_reaction(emoji)

@client.command()
async def crewwon(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Imposters Lost!', colour=discord.Color.red())
    embed.add_field(name="Imposters:", value=ctx.message.content.replace("!crewwon ", ""))
    embed.add_field(name="Timestamp:", value=ctx.message.created_at, inline=True)
    embed.set_thumbnail(url = "https://static.thenounproject.com/png/158126-200.png")
    embed.set_footer(text=f"Reported By: {ctx.author}", icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def imposterwon(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Congragulations Imposters!!', colour=discord.Color.gold())
    embed.add_field(name="Imposters:", value=ctx.message.content.replace("!imposterwon ", ""))
    embed.add_field(name="Timestamp:", value=ctx.message.created_at, inline=True)
    embed.set_thumbnail(url = "https://image.flaticon.com/icons/png/512/419/419952.png")
    embed.set_footer(text=f"Reported By: {ctx.author}", icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

client.run(token)
