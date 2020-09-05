import discord
import asyncio
from discord.ext import commands
from discord.ext.commands   import bot

# token = input("Input your Discord Bot's token.\n")
token = 'NzUwNjk3NjkyNjMxNTMxNTMw.X0-TtQ.Yl5gRibfBYwv4snJjtgzQAJpuGw'
# ITG
# amongVoiceChannel = 750634010723614741
# amongTextChannel = 750634259483590706
# fantasmikosChannel = 750691724589793291
# codeChannel = 750700369901912124
# fiotChannel = 690522033955799051

#hamborguesa
amongVoiceChannel = 747590796366053437
amongTextChannel = 750850108463120434
fantasmikosChannel = 708779003166851112
codeChannel = 750857189987713115

client = commands.Bot(command_prefix = "!")

client.remove_command("help")


# Starts the bot, with a status.
@client.event
async def on_ready():
    print('Among Us Bot is online!')
    await client.change_presence(status = discord.Status.online, activity=discord.Game('!help for commands'))


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


# Mute all players.
@client.command(aliases=['mute','m'])
async def mutePlayers(ctx):
    print("mute " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    fixed_channel = client.get_channel(amongVoiceChannel)
    members = fixed_channel.members #finds members connected to the channel
    # await ctx.send('Shhhh :shushing_face:')
    await ctx.send('Montero callate la puta boca :shushing_face:')
    for member in members:
        await member.edit(mute=True, deafen=True)

# Unmute all players.
@client.command(aliases=['unmute','u'])
async def unmutePlayers(ctx):
    print("unmute " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    among_channel = client.get_channel(amongVoiceChannel)
    among_members = among_channel.members #finds members connected to the channel
    fantasmikos_channel = client.get_channel(fantasmikosChannel)
    fantasmikos_members = fantasmikos_channel.members #finds members connected to the channel
    for member in fantasmikos_members:
        await member.edit(mute=False, deafen=False, voice_channel=among_channel)
    await ctx.send('A discutir :thinking:')
    for member in among_members:
        await member.edit(mute=False, deafen=False)

# Unmute all players.
@client.command(aliases=['fiot'])
async def fiotMeeting(ctx):
    print("fiot " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=1)
    among_channel = client.get_channel(fiotChannel)
    for member in ctx.guild.members:
        for role in member.roles: 
            if role.name == "FIOT": 
                await member.edit(mute=False, deafen=False, voice_channel=among_channel)

# Starts the game.
@client.command(aliases=['start', 's'])
async def startgame(ctx):
    print("startgame " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    embed = discord.Embed(title=f"{ctx.author} is starting a lobby!", description="Click the checkmark to ready up!", colour=discord.Color.blue())
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
        await fixed_channel.send(f'{user.mention} is ready to play! [{reaction.count - 1}/10]')


@client.event
async def on_reaction_remove(reaction, user):
    emoji = reaction.emoji
    if user.bot:
        return
    if emoji == '✅':
        fixed_channel = client.get_channel(amongTextChannel) # General / main chat channel ID
        await fixed_channel.send(f'{user.mention} is no longer ready to play! [{reaction.count - 1}/10]')


# Code command, gives the code to code channel. Usage is !code {insert code here}
@client.command(aliases=['c'])
async def code(ctx):
    print("code " + str(ctx.author) + " en " + str(ctx.channel))
    await ctx.channel.purge(limit=2)
    embed = discord.Embed(title='The Code for the game is:')
    embed.add_field(name='Code:', value=f"{ctx.message.content.replace('!code ', '').replace('!c ', '')}")
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
    embed = discord.Embed(title='Comandos del Among the Bot:', colour=discord.Color.blue())
    embed.add_field(name='Code (c) {code}', value='Envía al canal #code el código de la partida.')
    embed.add_field(name='startgame (s)', value='Comienza la partida y permite a los miembros estar listos')
    embed.add_field(name='Mute (m)', value='Mutea y ensordece a los miembros del canal ' + str(channelName) + '.')
    embed.add_field(name='unMute (u)', value='Desmutea y desensordece a los miembros del canal ' + str(channelName) + '.')
    embed.add_field(name='Ping', value='Muestra la lantencia de bot con los servidores de discord.')
    embed.add_field(name='cancelgame (cancel)', value='Muestra un mensaje indicando que se ha cancelado la partida.')
    embed.add_field(name='FalseAlarm', value='Echarle la culpa a alguien por una falsa alarma.')
    embed.add_field(name='StartGameNoPing', value='Empezar el juego, pero sin avisar.')
    embed.add_field(name='ImposterWon', value='!imposterwon {imposters}. Shows who the imposters were, and when they won!')
    embed.add_field(name='CrewWon', value='!crewwon {imposters}. Shows that the crew won and who the imposters were.')
    embed.add_field(name='HotKeys en el juego', value='Tab: ver el mapa \n Space, e: use')
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