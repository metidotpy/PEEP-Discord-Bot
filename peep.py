#import moduls
from asyncio import sleep
from collections import namedtuple
import json
import discord,random
from discord import client
from discord import embeds
from discord import colour
from discord import message
from discord import channel
from discord.embeds import Embed
from discord.ext import commands,tasks
from discord.voice_client import VoiceClient


#make a command prefix and client variable

client=commands.Bot(command_prefix="peep ", help_command=None)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="peep help"))
    print("WE ARE READY FOR NOW!")

#Error Handeling
@client.event
async def on_error_command(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed1=discord.Embed(
            name="Missing Arguments",
            colour=discord.Colour.blurple()
        )
        embed1.set_author(name=ctx.author.name,icon_url=ctx.author.icon_url)
        embed1.set_footer(text="Requested By {}".format(ctx.author),icon_url=ctx.author.avatar_url)
        embed1.add_field(name="Missing",value="Please Compelete All Arguments")
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingPermissions):
        embed2=discord.Embed(
            name="Missing Permision",
            colour=discord.Colour.blurple()
        )
        embed2.set_author(name=ctx.author.name,icon_url=ctx.author.icon_url)
        embed2.set_footer(text="Requested By {}".format(ctx.author),icon_url=ctx.author.avatar_url)
        embed2.add_field(name="Missing",value="Please Compelete All Arguments")
        await ctx.send(embed=embed2)

#sadPlaylists
sads=[]

#make sads from json files
with open("./json/sad_playlists.json", "r") as file_sad:
    sads = json.load(file_sad)

#lil peep random musics
peeps=[]

#make peeps from json files

with open("./json/peep_musics.json", "r") as file_peeps:
    peeps = json.load(file_peeps)


#lil peep random albums
albums=[]

#make albums from json files

with open("./json/peep_albums.json", "r") as file_albums:
    albums = json.load(file_albums)

#lil peep random playlist
playlists=[]

#make playlists from json files

with open("./json/peep_playlists.json", "r") as file_playlist:
    playlists = json.load(file_playlist)

#lil peep random music videos
videos=[]

#make videos from json files

with open("./json/peep_videos.json", "r") as file_videos:
    videos = json.load(file_videos)

#lil peep slowed and reverbs song
slowed=[]

#make slowed from json files

with open("./json/peep_slowed.json", "r") as file_slowed:
    slowed = json.load(file_slowed)

#lil peep live musics
lives=[]

#make lives from json files

with open("./json/peep_lives.json", "r") as file_lives:
    lives = json.load(file_lives)

#lil peep covers
covers=[]

#make covers from json files

with open("./json/peep_covers.json", "r") as file_covers:
    covers = json.load(file_covers)


#make help command
@client.command(aliases=["help"])
async def _help(ctx):
    embed=discord.Embed(
        title="Help Command",
        colour=discord.Colour.blue()
    )
    embed.add_field(name="BioGraphy",value="**`bio`**, **`biography`**, **`born`**",inline=False)
    embed.add_field(name="Make RIP",value="**`rest`**, **`rip`**, **`restinpeace`**, **`respect`**",inline=False)
    embed.add_field(name="Sad Musics",value="**`sad`**, **`playlist`**, **`sad_musics`**",inline=False)
    embed.add_field(name="Lil Peep Musics",value="**`sadpeep`**, **`peepsad`**, **`peep`**, **`random`**, **`music`**",inline=False)
    embed.add_field(name="All Music ",value="**`full`**, **`all`**, **`full_music`**",inline=False)
    embed.add_field(name="Random ALbums",value="**`peepalbum`**, **`albumpeep`**, **`album`**, **`randomalbum`**",inline=False)
    embed.add_field(name="Random Playlists",value="**`peeplist`**, **`listpeep`**, **`randompeeplist`**, **`playpeep`**",inline=False)
    embed.add_field(name="Random Slowed and Reverb Songs",value="**`slowed`**, **`peepslowed`**, **`slowedpeep`**, **`slow`**, **`reverb`**, **`peepreverb`**, **`reverbpeep`**",inline=False)
    embed.add_field(name="Random Music Video",value="**`peepvideo`**, **`videopeep`**, **`video`**, **`musicvideo`**",inline=False)
    embed.add_field(name="Random Live Music",value="**`live`**, **`peeplive`**, **`livepeep`**",inline=False)
    embed.add_field(name="Random Cover Music",value="**`cover`**, **`peepcover`**, **`coverpeep`**",inline=False)
    embed.add_field(name="Meti's Playlist",value="**`deadonthecode`**, **`deadonthecode2`**, **`deadbody`**, **`dead`**",inline=False)
    embed.add_field(name="Version",value="version",inline=False)
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Requested By {}".format(ctx.author),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
#lil peep biography
@client.command(aliases=["bio","biography","born"])
async def _bio(ctx):
    embed=discord.Embed(
        name="Lil Peep Biography",
        colour=discord.Colour.dark_grey()
    )
    embed.add_field(name="Who Is Lil Peep",value='''
Lil Peep was born on November 1, 1996 in Allentown, Pennsylvania, USA as Gustav Elijah Åhr. He is known for his work on Lil Peep, feat. iLoveMakonen: I've Been Waiting (Original Version) (Audio) (2019), Lil Peep Feat. Clams Casino: 4 Gold Chains (2018) and Lil Peep: Drugz (2020). He died on November 15, 2017 in Tucson, Arizona, USA.   
''')
    embed.set_image(url="https://cdn.discordapp.com/attachments/837344763580776519/844784946454855710/profilephoto.jpg")
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Requested By {}".format(ctx.author),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
#rest in peace for lil peep
@client.command(aliases=["rest","rip","restinpeace","respect"])
async def _rest(ctx):
    embed=discord.Embed(
        name="Rest In Peace",
        colour=discord.Colour.dark_grey()
    )
    embed.add_field(name="RIP",value="REST IN PEACE :), I LOVE YOUR SONG! :)")
    embed.set_image(url="https://cdn.discordapp.com/attachments/837344763580776519/844784946454855710/profilephoto.jpg")
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Requested By {}".format(ctx.author),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)




# found some random play list sad
@client.command(aliases=["sad","playlist","sad_musics"])
async def _sad(ctx):
    global sads
    await ctx.send(
        f"""
**`A Sad Play List :)`**
{random.choice(sads)}
        """
    )

#lil peep random music
@client.command(aliases=["sadpeep","peep","music","random","peepsad"])
async def _sadpeep(ctx):
    global peeps
    await ctx.send(
f'''
**`A Random PEEP Music:)`**
{random.choice(peeps)}
'''
    )
#full musics from lil peep
@client.command(aliases=["full","all","full_music"])
async def _full(ctx):
    await ctx.send(
'''
**`Full Musics :)`**
https://soundcloud.com/lilpeepnite2/sets/all-lil-peep-songs-singles
'''
    )

#random albums
@client.command(aliases=["album","peepalbum","randomalbum","albumpeep"])
async def _albun(ctx):
    global albums
    await ctx.send(
f'''
**`lil peep random album :)`**
{random.choice(albums)}
'''
    )
#random lil peep playlist
@client.command(aliases=["peeplist","playpeep","randompeeplist","listpeep"])
async def _peeplist(ctx):
    global playlists
    await ctx.send(
f'''
**`lil peep random playlist`**
{random.choice(playlists)}
'''
    )

#peep random music videos
@client.command(aliases=["peepvideo","musicvideo","video","videopeep"])
async def _peepvideo(ctx):
    global videos
    await ctx.send(
f'''
**`lil peep music videos :)`**
{random.choice(videos)}
'''
    )

#lil peep random slowed and reverbs song
@client.command(aliases=["slowed","peepslowed","slow","slowedpeep","reverb","peepreverb","reverbpeep"])
async def _slowed(ctx):
    await ctx.send(
f'''
**`lil peep random slowed & reverb musics :)`**
{random.choice(slowed)}
'''
    )

#lil peep random live musics
@client.command(aliases=["live","peeplive","livepeep"])
async def _live(ctx):
    await ctx.send(
f'''
**`lil peep random live musics :)`**
{random.choice(lives)}
'''
    )
#lil peep random covers
@client.command(aliases=["cover","peepcover","coverpeep"])
async def _cover(ctx):
    await ctx.send(
f'''
**`lil peep random cover musics :)`**
{random.choice(covers)}
'''
    )

#dead on the codes
@client.command()
async def deadonthecode(ctx):
    await ctx.send(
'''
**`Dead On The Code :)`**
https://music.youtube.com/playlist?list=PLfr2oiPg9Y3_FbshdDQU7mQLBZnx31S9J&feature=share
'''
    )

@client.command()
async def deadonthecode2(ctx):
    await ctx.send(
'''
**`Dead On The Code,Vol 2 :)`**
https://music.youtube.com/playlist?list=PLfr2oiPg9Y38uTISKi6fWfYfSPlh6lZe0&feature=share
'''
    )

@client.command()
async def deadbody(ctx):
    await ctx.send(
'''
**`Dead Body :)`**
https://music.youtube.com/playlist?list=PLfr2oiPg9Y3_13IfUuZzbvC2ZhlTWqpOr&feature=share
'''
    )

@client.command()
async def dead(ctx):
    await ctx.send(
'''
**`Dead :)`**
https://music.youtube.com/playlist?list=PLfr2oiPg9Y38FBToasI37xwZnovu9c_jm&feature=share
'''
    )


#join channel command
@client.command(pass_context=True)
async def join(ctx):
    # channel=ctx.message.author.voice.channel
    # await client.join_voice_channel(channel)
    # author = ctx.message.author
    # channel = author.voice_channel
    # await client.join_voice_channel(channel)
    channel = ctx.author.voice.channel
    await channel.connect()
    msg=await ctx.send("Join The Your Channel")
    await sleep(4)
    await msg.delete()
    await sleep(4)
    
@client.command(pass_context=True)
async def leave(ctx):
    # server=ctx.message.server
    # voice_client=client.voice_client_in(server)
    # await voice_client.disconnect()
    await ctx.voice_client.disconnect()
    msg=await ctx.send("Leave From Your Channel")
    await sleep(4)
    await msg.delete()
    await sleep(4)



#
@client.command(name="version")
async def _version(ctx):
    await ctx.send("**PEEP Version Is 1.2**")

client.run("ODQ0NzM1MjQ0NjQ4MTg1ODc2.YKWvAA.rnl_1M_DD9Y2bYOZXHVmtR_ioeM")