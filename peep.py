#import moduls
from asyncio import sleep
from collections import namedtuple
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
sads=[
    "https://open.spotify.com/playlist/7ABD15iASBIpPP5uJ5awvq",
    "https://www.youtube.com/watch?v=AkBLnEqmkqU",
    "https://soundcloud.com/stylezmajor/sets/1-sad-music-playlist-2020",
    "https://soundcloud.com/auroravibesyt/depressing-songs-1-hour",
    "https://soundcloud.com/user-566997069/sets/xxx-sad-nibba-hours-playlist",
    "https://soundcloud.com/bansemerchloe/sets/sad-playlists",
    "https://www.youtube.com/watch?v=GOjsIgeRhYU",
    "https://www.youtube.com/watch?v=bv26oe1I7Dc",
    "https://www.youtube.com/watch?v=Y_oD111dK7c",
    "https://www.youtube.com/playlist?list=PLyORnIW1xT6wOsrPFVQ5AiR9P2VyArzj4",
    "https://www.youtube.com/watch?v=yazfWjaetXA",
    "https://www.youtube.com/watch?v=s7FTAxw37hk",
    "https://www.youtube.com/watch?v=T8-96tqFCFU",
    "https://www.youtube.com/watch?v=SbNDmAJBtyU",
    "https://www.youtube.com/watch?v=Jllu94-8PxI",
    "https://www.youtube.com/watch?v=kpcWrpt1Kl0",
    "https://www.youtube.com/playlist?list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy",
    "https://www.youtube.com/watch?v=SIHDpxLA-kE",
    "https://www.youtube.com/watch?v=VVcYlVQXj_s",
    "https://www.youtube.com/watch?v=z_m5VoytV1Q",
    "https://www.youtube.com/watch?v=YHi7Y0iaUo4",
    "https://www.youtube.com/watch?v=dTxTUDL4A-E",
    "https://www.youtube.com/watch?v=KLNCZxzI27A",
    "https://www.youtube.com/watch?v=CXXK371s5mA",
    "https://www.youtube.com/watch?v=PT2wsfdnymA",
    "https://www.youtube.com/watch?v=F81EqiVBLb4",
    "https://www.youtube.com/watch?v=7UxZtzyl8Xw",
    "https://www.youtube.com/watch?v=CkJ6w-V54EA",
    "https://www.youtube.com/watch?v=pJ_m5lDftYc",
    "https://www.youtube.com/watch?v=YrjZ7rE5ous",
    "https://www.youtube.com/watch?v=CXXK371s5mA",
    "https://www.youtube.com/watch?v=Pzc_3arId8s",
    "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "https://open.spotify.com/playlist/7ABD15iASBIpPP5uJ5awvq",
    "https://open.spotify.com/playlist/6XFfCL23a4TwyxuhEY2cXb",
    "https://open.spotify.com/playlist/6XFfCL23a4TwyxuhEY2cXb",
    "https://open.spotify.com/playlist/014vY40mh7KcAnCsCwEJVo",
    "https://open.spotify.com/playlist/014vY40mh7KcAnCsCwEJVo",
    "https://open.spotify.com/playlist/78FHjijA1gBLuVx4qmcHq6",
    "https://open.spotify.com/playlist/4WloBZWLuV80F07SCPxs09",
    "https://open.spotify.com/playlist/6ZT2VoUIoRXITfHl0YNpcV",
    "https://open.spotify.com/playlist/37i9dQZF1DWZUAeYvs88zc",

]
#lil peep random musics
peeps=[
    "https://soundcloud.com/lil_peep/california-world-feat-craig-xen",
    "https://soundcloud.com/lil_peep/lil-kennedy",
    "https://soundcloud.com/lil_peep/drive-by-w-xavier-wulf-2020-prod-nedarb",
    "https://soundcloud.com/lil_peep/drugz",
    "https://soundcloud.com/lil_peep/mos-battery-full",
    "https://soundcloud.com/lil_peep/shiver",
    "https://soundcloud.com/lil_peep/come-around",
    "https://soundcloud.com/lil_peep/walk-away-as-the-door-slams-acoustic-ft-lil-tracy",
    "https://soundcloud.com/lil_peep/witchblades-ft-lil-tracy",
    "https://soundcloud.com/lil_peep/Keep-My-Coo",
    "https://soundcloud.com/lil_peep/ghost_boy",
    "https://soundcloud.com/lil_peep/ive-been-waiting-original-version-ft-ilovemakonnen",
    "https://soundcloud.com/lil_peep/princess",
    "https://soundcloud.com/lil_peep/text-me-ft-era",
    "https://soundcloud.com/lil_peep/rockstarz-ft-gab3",
    "https://soundcloud.com/lil_peep/la-to-london-ft-gab3",
    "https://soundcloud.com/lil_peep/fangirl-ft-gab3",
    "https://soundcloud.com/lil_peep/ratchets-w-lil-tracy-diplo",
    "https://soundcloud.com/lil_peep/aquafina-ft-rich-the-kid",
    "https://soundcloud.com/lil_peep/liar",
    "https://soundcloud.com/lil_peep/moving-on",
    "https://soundcloud.com/lil_peep/belgium",
    "https://soundcloud.com/lil_peep/when-i-lie",
    "https://soundcloud.com/lil_peep/lil-peep-xxxtentacion-falling-down-travis-barker-remix",
    "https://soundcloud.com/lil_peep/when-i-lie-remix-feat-ty-dolla",
    "https://soundcloud.com/lil_peep/lil-peep-ilovemakonnen-feat-fall-out-boy-ive-been-waiting",
    "https://soundcloud.com/lil_peep/broken-smile-my-all",
    "https://soundcloud.com/lil_peep/sex-with-my-ex",
    "https://soundcloud.com/lil_peep/leanin",
    "https://soundcloud.com/lil_peep/16-lines",
    "https://soundcloud.com/lil_peep/hate-me",
    "https://soundcloud.com/lil_peep/idgaf",
    "https://soundcloud.com/lil_peep/white-girl",
    "https://soundcloud.com/lil_peep/fingers",
    "https://soundcloud.com/lil_peep/life-is-beautiful",
    "https://soundcloud.com/lil_peep/runaway",
    "https://soundcloud.com/lil_peep/cryalone",
    "https://soundcloud.com/lil_peep/lil-peep-makonnen-sunlight-on-your-skin",
    "https://soundcloud.com/lil_peep/lil-peep-ft-xxxtentacion-falling-down",
    "https://soundcloud.com/lil_peep/4-gold-chains-feat-clams",
    "https://soundcloud.com/lil_peep/spotlight-1",
    "https://soundcloud.com/lil_peep/lil-peep-feat-wicca-doves-avoid-eq",
    "https://soundcloud.com/lil_peep/better-off-dying",
    "https://soundcloud.com/lil_peep/u-said",
    "https://soundcloud.com/lil_peep/awful-things",
    "https://soundcloud.com/lil_peep/save-that-shit",
    "https://soundcloud.com/lil_peep/problems",
    "https://soundcloud.com/lil_peep/the-brightside-prod-smokeasac",
    "https://soundcloud.com/lil_peep/benz-truck",
    "https://soundcloud.com/lil_peep/beamer-boy",
    "https://soundcloud.com/lil_peep/absolute-in-doubt-feat-wicca",
    "https://soundcloud.com/lil_peep/no-respect-freestyle-prod-greaf",
    "https://soundcloud.com/lil_peep/lil-peep-lil-tracy-prod-cortex-sincewhen",
    "https://soundcloud.com/lil_peep/stop-the-car-w-horsehead-prod-smokeasac",
    "https://soundcloud.com/lil_peep/kisses-in-the-wind-w-lil-tracy-prod-dirty-vans",
    "https://soundcloud.com/lil_peep/smokepurpp-on-a-bean-prod-willie-g",
    "https://soundcloud.com/lil_peep/giving-girls-cocaine-w-lil-tracy-prod-horsehead",
    "https://soundcloud.com/lil_peep/right-here-w-horse-head-prod-nedarb",
    "https://soundcloud.com/lil_peep/love-letter-prod-charlie-shuffler",
    "https://soundcloud.com/lil_peep/kiss-prod-smokeasac",
    "https://soundcloud.com/lil_peep/about-u-prod-brobak",
    "https://soundcloud.com/lil_peep/prada-prod-lederrick",
    "https://soundcloud.com/lil_peep/walk-away-as-the-door-slams-prod-yung-cortex",
    "https://soundcloud.com/lil_peep/the-last-thing-i-wanna-do-prod-smokeasac",
    "https://soundcloud.com/lil_peep/we-think-too-much-prod-nedarb",
    "https://soundcloud.com/lil_peep/nose-ring-prod-cian-p",
    "https://soundcloud.com/lil_peep/girls-w-horsehead-prod-dirty-vans",
    "https://soundcloud.com/lil_peep/girls-w-horsehead-prod-dirty-vans",
    "https://soundcloud.com/lil_peep/red-drop-shawty-w-kirblagoop-prod-charlie-shuffler",
    "https://soundcloud.com/lil_peep/worlds-away-prod-horse-head",
    "https://soundcloud.com/lil_peep/interlude-prod-brobak",
    "https://soundcloud.com/lil_peep/gucci-mane-prod-charlie-shuffler",
    "https://soundcloud.com/lil_peep/cobain-w-lil-tracy-prod-smokeasac",
    "https://soundcloud.com/lil_peep/fucked-up-prod-horse-head",
    "https://soundcloud.com/lil_peep/the-song-they-played-when-i-crashed-into-the-wall-w-lil-tracy-prod-smokeasac",
    "https://soundcloud.com/lil_peep/omfg-prod-nedarb",
    "https://soundcloud.com/lil_peep/drive-by-w-xavier-wulf-prod-nedarb",
    "https://soundcloud.com/lil_peep/hellboy-prod-smokeasac-x-yung-cortex",
    "https://soundcloud.com/lil_peep/move-on-be-strong-prod-smokeasac-x-lil-peep-x-yung-cortex",
    "https://soundcloud.com/lil_peep/sex-last-nite-prod-smokeasac-x-yung-cortex",
    "https://soundcloud.com/lil_peep/white-wine-prod-nedarb",
    "https://soundcloud.com/lil_peep/castles-prod-nedarb",
    "https://soundcloud.com/lil_peep/pain-w-slug-christ-prod-nedarb",
    "https://soundcloud.com/lil_peep/white-tee-w-yung-bruh-prod-nedarb",
    "https://soundcloud.com/lil_peep/falling-4-meprod-lederrick-x-horse-head",
    "https://soundcloud.com/lil_peep/skyscrapers-love-now-cry-later-prod-jayyeah",
    "https://soundcloud.com/lil_peep/big-city-blues-ft-coldhart",
    "https://soundcloud.com/lil_peep/absolute-in-doubt-w-wicca-phase-springs-eternal-prod-foxwedding",
    "https://soundcloud.com/lil_peep/yesterday-prod-charlie-shuffler",
    "https://soundcloud.com/lil_peep/lil-jeep-prod-cian-p",
    "https://soundcloud.com/lil_peep/crybaby-prod-lederrick-x-lil-peep",
    "https://soundcloud.com/lil_peep/driveway-prod-smokeasac",
    "https://soundcloud.com/lil_peep/ghost-girl-prod-lederrick",
    "https://soundcloud.com/lil_peep/nineteen-prod-smokeasac",
    "https://soundcloud.com/lil_peep/gym-class-prod-brobak",
    "https://soundcloud.com/lil_peep/your-eyes-prod-lederrick",
    "https://soundcloud.com/lil_peep/pray-i-die-prod-nedarb-nagrom",
    "https://soundcloud.com/lil_peep/beat-it-prod-nedarb-nagrom",
    "https://soundcloud.com/lil_peep/beamerboy-prod-nedarb-nagrom",
    "https://soundcloud.com/lil_peep/let-me-bleed-prod-nedarb-nagrom",
    "https://soundcloud.com/lil_peep/pick-me-up-ft-yunggoth-prod-fleance",
    "https://soundcloud.com/lil_peep/nuts-ft-lil-skil-prod-willie-g",
    "https://soundcloud.com/lil_peep/live-forever-prod-brobak",
    "https://soundcloud.com/lil_peep/the-way-i-see-things-prod-kryptik",
    "https://soundcloud.com/lil_peep/star-shopping-prod-kryptik",
    "https://soundcloud.com/lil_peep/praying-to-the-sky-prod-greaf",
    "https://soundcloud.com/lil_peep/lil-peep-x-greaf"
]
#lil peep random albums
albums=[
    "https://soundcloud.com/user-962807485-41097447/sets/hate-me",
    "https://soundcloud.com/gus-ahrchive/sets/feelz",
    "https://soundcloud.com/user-908711570-337077758/sets/lil-peep-part-one",
    "https://soundcloud.com/skeletonsarchive3/sets/lil-peep-live-forever",
    "https://soundcloud.com/lil_peep/sets/vertigo",
    "https://soundcloud.com/user-962807485-41097447/sets/california-girls",
    "https://soundcloud.com/lilpeepnite2/sets/lil-peep-crybaby-full-mixtape",
    "https://soundcloud.com/user-962807485-41097447/sets/teen-romance",
    "https://soundcloud.com/lilpeepnite2/sets/lil-peep-hellboy-full-mixtape",
    "https://soundcloud.com/lil_peep/sets/come-over-when-youre-sober",
    "https://soundcloud.com/lil_peep/sets/come-over-when-youre-sober-pt",
    "https://soundcloud.com/lil_peep/sets/goth-angel-sinner",
    "https://soundcloud.com/lil_peep/sets/everybodys-everything",
    "https://soundcloud.com/user-847395860/sets/come-over-when-your-sober"
]

#lil peep random playlist
playlists=[
    "https://www.youtube.com/watch?v=IoFeOi0vShs",
    "https://www.youtube.com/playlist?list=PLhIwhNQef1R8ie4sbPufnjmemC2H6yp-Z",
    "https://www.youtube.com/watch?v=POBPP4aD704",
    "https://www.youtube.com/watch?v=eTAtFKti7rY",
    "https://www.youtube.com/watch?v=ebWauDTTf3s",
    "https://www.youtube.com/watch?v=FBhfUXoLKJQ",
    "https://www.youtube.com/watch?v=waJt6AWSXDI",
    "https://www.youtube.com/playlist?list=PLtjq7jwCVgmjYnZNBPWQglc3GQpjAe7f-",
    "https://soundcloud.com/7illme/sets/lil-peep-playlist",
    "https://soundcloud.com/user-949344446/sets/lil-peep-playlist",
    "https://soundcloud.com/lljseren/sets/best-lil-peep-playlist",
    "https://soundcloud.com/user-8000508/sets/lil-peep-playlist",
    "https://soundcloud.com/user-528845277/sets/lil-peep-playlist",
    "https://soundcloud.com/user-594978842/sets/updated-lil-peep-playlist",
    "https://soundcloud.com/user884091856/sets/lil-peep-playlist",
    "https://soundcloud.com/cj-brown-19989356/lil-peep-rare-mix-lost-song",
    "https://soundcloud.com/teerog/sets/godtier-lil-peep-playlist",
    "https://soundcloud.com/user-647524837/sets/lil-peep-playlist",
    "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1kxsTC",
    "https://open.spotify.com/playlist/6jxv9ccQTxEerkjY3ajzJv",
    "https://open.spotify.com/playlist/6m98lYCplafZzdSGQQSg7j",
    "https://open.spotify.com/playlist/7Iz9KWo1ltVsCmDR3OEVsU",
    "https://open.spotify.com/playlist/1apQLxMsC1RiYarqFdfsMD",
    "https://open.spotify.com/playlist/49MeigGKPwj6aZu1rTP71g",
    "https://soundcloud.com/j4k37/sets/sad-peep",
    "https://soundcloud.com/user-327052624/sets/lil-peep-sad-playlist",
    "https://soundcloud.com/producerlow/sets/lil-peep-sad-songs-only",
    "https://soundcloud.com/1december1/sets/top-10-saddest-lil-peep-songs",
    "https://soundcloud.com/hengoski/sets/lil-peep-sad-songs",
    "https://soundcloud.com/hateee-95227341/sets/lilpeep",
    "https://soundcloud.com/vh-ryu/sets/sad-lil-peep-playlist",
    "https://soundcloud.com/user-549513904/sets/sad-lil-peep-songs",
    "https://www.youtube.com/watch?v=waJt6AWSXDI",
    "https://www.youtube.com/watch?v=yfs2toNqBFY",
    "https://www.youtube.com/watch?v=ksiqkLxtef4",
    "https://www.youtube.com/watch?v=POBPP4aD704",
    "https://www.youtube.com/watch?v=Mh7IXXgqNOM",
    "https://www.youtube.com/watch?v=arKr_2iUf9g",
    "https://www.youtube.com/watch?v=guCRd_NxkRk",
    "https://www.youtube.com/watch?v=eM4VyHqEbLk",
    "https://www.youtube.com/watch?v=HM3HUtNIxW8",
    "https://www.youtube.com/watch?v=00oCURtmcKY",
    "https://www.youtube.com/watch?v=qNvviYlHZCA",
    "https://www.youtube.com/watch?v=UMml2JvnMmQ",
    "https://www.youtube.com/watch?v=ebWauDTTf3s",
    "https://www.youtube.com/playlist?list=PLpXA1IqBgeZTs86Qq7cz1dNAeA8NwM5Qu",
    "https://www.youtube.com/playlist?list=PL_Yz3-t_nXBcQ58rvyEXShK131liV4A1r",
    "https://www.youtube.com/watch?v=tjOGgmpb90A",
    "https://www.youtube.com/watch?v=eTAtFKti7rY",
    "https://www.youtube.com/watch?v=93M0-QbD6fI"
]

#lil peep random music videos
videos=[
    "https://www.youtube.com/watch?v=aEnV66QkwNk&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=1",
    "https://www.youtube.com/watch?v=JtRcHPXclhE&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=2",
    "https://www.youtube.com/watch?v=cQAIac02jKE&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=3",
    "https://www.youtube.com/watch?v=WA3VEhbvwRY&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=4",
    "https://www.youtube.com/watch?v=PKalQrHXayI&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=5",
    "https://www.youtube.com/watch?v=mwrTFbnZEjA&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=6",
    "https://www.youtube.com/watch?v=7Bbv6gL-NAA&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=8",
    "https://www.youtube.com/watch?v=ayy6AbMUkG8&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=10",
    "https://www.youtube.com/watch?v=fudsUhWAG_o&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=12",
    "https://www.youtube.com/watch?v=hSRFglBAN94&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=14",
    "https://www.youtube.com/watch?v=wckAAh-V428&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=15",
    "https://www.youtube.com/watch?v=heJNHYCSsIc&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=13",
    "https://www.youtube.com/watch?v=3hlSgENWCcU&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=16",
    "https://www.youtube.com/watch?v=l2liKZDH-0c&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=17",
    "https://www.youtube.com/watch?v=E7sP6t1QyrI&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=18",
    "https://www.youtube.com/watch?v=1ErdExuCuxM&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=19",
    "https://www.youtube.com/watch?v=Mu5xpZdYoQ0&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=21",
    "https://www.youtube.com/watch?v=3rkJ3L5Ce80&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=22",
    "https://www.youtube.com/watch?v=QbgaRbyWTW8&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=23",
    "https://www.youtube.com/watch?v=haPbNGXAzx8&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=24",
    "https://www.youtube.com/watch?v=xAMgQQMZ9Lk&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=25",
    "https://www.youtube.com/watch?v=zOujzvtwZ6M&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=26",
    "https://www.youtube.com/watch?v=hqH3MTF2ZfM&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=27",
    "https://www.youtube.com/watch?v=GEK6RkPqoOU&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=28",
    "https://www.youtube.com/watch?v=WvV5TbJc9tQ&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=29",
    "https://www.youtube.com/watch?v=q0KtW7J_d4c&list=PL1ezV3fe3WY5rjcR9b7FvwSTehnlpnOzN&index=30",
    "https://www.youtube.com/watch?v=DxNt7xV5aII",
    "https://www.youtube.com/watch?v=s9t1ZfMZfH4",
    "https://www.youtube.com/watch?v=9YJQgfSdL3k&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=4",
    "https://www.youtube.com/watch?v=0_RowQgiERI&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=32",
    "https://www.youtube.com/watch?v=7R1N-8SoqcM&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=31",
    "https://www.youtube.com/watch?v=2ORsrbQa94M&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=36",
    "https://www.youtube.com/watch?v=zUPPrimH7Ow&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=44",
    "https://www.youtube.com/watch?v=PI6YVmL6U68&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=45",
    "https://www.youtube.com/watch?v=eIDySR4SFZI&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=40",
    "https://www.youtube.com/watch?v=fzV_QZODisQ&list=PLaGNXpUYDxPqBqTvaJ3XBYSXmDSdUDg7f&index=34"
]

#lil peep slowed and reverbs song
slowed=[
    "https://soundcloud.com/peepslowedsongs/lil-peep-five-degrees-slow-reverb",
    "https://soundcloud.com/peepslowedsongs/lil-peep-gym-class-slow-reverb",
    "https://soundcloud.com/peepslowedsongs/lil-peep-mud-on-my-gucci-slow-reverb",
    "https://soundcloud.com/peepslowedsongs/lil-peep-yunggoth-pick-me-up-slow-reverb",
    "https://soundcloud.com/peepslowedsongs/lil-peep-lil-tracy-white-tee-slow-reverb",
    "https://soundcloud.com/peepslowedsongs/anothersong",
    "https://soundcloud.com/peepslowedsongs/beatit",
    "https://soundcloud.com/peepslowedsongs/bitchimakillyou",
    "https://soundcloud.com/peepslowedsongs/crybaby",
    "https://soundcloud.com/peepslowedsongs/driveway",
    "https://soundcloud.com/peepslowedsongs/giveuthemoon",
    "https://soundcloud.com/peepslowedsongs/letitflow",
    "https://soundcloud.com/peepslowedsongs/lietome",
    "https://soundcloud.com/peepslowedsongs/lilkennedy",
    "https://soundcloud.com/peepslowedsongs/prayidie",
    "https://soundcloud.com/peepslowedsongs/smokepurpponabean",
    "https://soundcloud.com/peepslowedsongs/teenromance",
    "https://soundcloud.com/peepslowedsongs/thewayiseethings",
    "https://soundcloud.com/peepslowedsongs/wethinktoomuch",
    "https://soundcloud.com/sad-slowed-down/lil-peep-xxxtentacion-falling-down-slowed-reverb",
    "https://soundcloud.com/exstacy-750149327/nuts-lil-peep-slowed-reverb",
    "https://soundcloud.com/wrathslowed/lil-peep-star-shopping-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-tracy-lil-peep-your-favorite-dress-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-cobain-w-lil-tracy-slowed-reverb",
    "https://soundcloud.com/bishopkane/beamer-boy-slowed-and-reverb",
    "https://soundcloud.com/dumbkid4ever/lil-peep-16-lines-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-omfg-8d-audio-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-save-that-shit-8d-slowed-reverb",
    "https://soundcloud.com/wrathslowed/lil-peep-benz-truck-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-praying-to-the-sky-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-nothing-to-u-slowed-reverb",
    "https://soundcloud.com/yungslater/lil-peep-tracy-giving-girls-cocaine-slowed-reverb",
    "https://soundcloud.com/suicidez/lil-peep-sex-with-my-ex-og-slowedreverb",
    "https://soundcloud.com/pgltm/california-world-lil-peep-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-feelz-slowed-reverb",
    "https://soundcloud.com/archiveplusplus/lil-peep-x-horse-head-right-here-slowed-reverb",
    "https://soundcloud.com/archiveplusplus/lil-peep-x-lil-tracy-dying-out-west-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-tonight-slowed-reverb",
    "https://soundcloud.com/idanked-bass-boosted/haunt-u-w-lil-peep-bass-1",
    "https://soundcloud.com/michael-mattessich/lil-peep-fingers-slowed-reverb",
    "https://soundcloud.com/user-391251155/lil-peep-bullet-slowed-reverb",
    "https://soundcloud.com/user-391251155/waste-of-time-lil-peep-without-bathsaltbryce-slowed-reverb-extended-lyrics",
    "https://soundcloud.com/user-306262264/lil-peep-ghost-girl-slowed-reverb",
    "https://soundcloud.com/matt-barr-751282972/lil-peep-better-off-dying-slowed-reverb",
    "https://soundcloud.com/jtslowed/lil-peep-4-gold-chains-ft-clams-casino-slowed-reverb",
    "https://soundcloud.com/wrathslowed/lil-peep-give-u-the-moon-slowed-reverb",
    "https://soundcloud.com/sternmark/yesterday-lil-peep-slowed-verision",
    "https://soundcloud.com/hasumu/lil-peep-u-said-slowed-reverb",
    "https://soundcloud.com/user-763199435/cold-hart-lil-peep-me-and-you-slowed-reverb",
    "https://soundcloud.com/glossgawd/lil-peep-about-u-slowed-reverb",
    "https://soundcloud.com/archiveplusplus/lil-peep-x-lil-tracy-i-crash-you-crash-slowed-reverb",
    "https://soundcloud.com/skrxxws/lil-peep-absolute-in-doubt-slowed-reverbdelay",
    "https://soundcloud.com/313newsnickers/lil-peep-dont-panic",
    "https://soundcloud.com/user-306262264/smokeasac-overdose-ft-lil-peep-x-lil-tracy-slowed-reverb",
    "https://soundcloud.com/white-savage-704588476/lil-peep-broken-smile-oldslowedreverb",
    "https://soundcloud.com/user-521137190/lil-peep-ft-juice-wrld-idgaf",
    "https://soundcloud.com/user-297878873/lil-peep-moving-on-slowed-rain-reverb",
    "https://soundcloud.com/chxris/lil-peep-the-way-i-see-things-slowedreverb-and-rain"
]
#lil peep live musics
lives=[
    "https://www.youtube.com/watch?v=YzIZXiG3gXk",
    "https://www.youtube.com/watch?v=5mqd4l6dhWg",
    "https://www.youtube.com/watch?v=M9N2EKE_5BI",
    "https://www.youtube.com/watch?v=v_zlw55gLTc",
    "https://www.youtube.com/watch?v=5ORJ9yGaqRc",
    "https://www.youtube.com/watch?v=z6kk377l1m4",
    "https://www.youtube.com/watch?v=Txj4ehuDDq0",
    "https://www.youtube.com/watch?v=rWtfX0jZZP0",
    "https://www.youtube.com/watch?v=j0a_2czRuGk",
    "https://www.youtube.com/watch?v=87aMWOkNni0",
    "https://www.youtube.com/watch?v=1bHylk9_GwQ",
    "https://www.youtube.com/watch?v=uZVLv0yCyG8",
    "https://www.youtube.com/watch?v=GL7Qd4BFPnE",
    "https://www.youtube.com/watch?v=0T7BX0oJQjE",
    "https://www.youtube.com/watch?v=i7GTDv6adVY",
    "https://www.youtube.com/watch?v=jhjKwOEaJTc",
    "https://www.youtube.com/watch?v=2YErDmoAsMU",
    "https://www.youtube.com/watch?v=5ecbjBK7euM",
    "https://www.youtube.com/watch?v=Wbox5VYEz1Q",
    "https://www.youtube.com/watch?v=VG9spvZxHAs",
    "https://www.youtube.com/watch?v=wcsaLTfhxQo",
    "https://www.youtube.com/watch?v=4RiQIo-B2KI",
    "https://www.youtube.com/watch?v=c_rMC5cC4Fk",
    "https://www.youtube.com/watch?v=ArFpbFYBgkc",
    "https://www.youtube.com/watch?v=L6hV-tmRc_c",
    "https://www.youtube.com/watch?v=I96QuzMR3pM",

]
#lil peep covers
covers=[
    "https://www.youtube.com/watch?v=XmOpuq64EUs",
    "https://www.youtube.com/watch?v=oJpk3pCWKKA",
    "https://www.youtube.com/watch?v=dqn7B3rUTUg",
    "https://www.youtube.com/watch?v=iyzS4T0LQCE",
    "https://www.youtube.com/watch?v=i-nYAwiyy0Q",
    "https://www.youtube.com/watch?v=bDoFJDXPFxg",
    "https://www.youtube.com/watch?v=2z_pvYGK-8E",
    "https://www.youtube.com/watch?v=PPzDv2jjR3g",
    "https://www.youtube.com/watch?v=WLHxBb4ZDwM",
    "https://www.youtube.com/watch?v=dHAgghjv0t0",
    "https://www.youtube.com/watch?v=4Z9tt3C1ocA",
    "https://www.youtube.com/watch?v=k44riOLgxMs",
    "https://www.youtube.com/watch?v=5fLXi9tABu0",
    "https://www.youtube.com/watch?v=f760fM68bDo",
    "https://www.youtube.com/watch?v=Lj80NDkLEGw",
    "https://www.youtube.com/watch?v=qKTBVU2VTPw",
    "https://www.youtube.com/watch?v=u0DLP6VmOww",
    "https://www.youtube.com/watch?v=QrDqAQpwXCc",
    "https://www.youtube.com/watch?v=zN5wQx7hxLY",
    "https://www.youtube.com/watch?v=3DPz6TR7KcQ",
    "https://www.youtube.com/watch?v=Pwv-5AaNi84",
    "https://www.youtube.com/watch?v=pViIZnkY8Rw",
    "https://www.youtube.com/watch?v=7EbMHp2QOJs",
    "https://www.youtube.com/watch?v=LeI-6ZRps4s",
    "https://www.youtube.com/watch?v=x1JtutI72Qk",
    "https://www.youtube.com/watch?v=PNqYuO-0y3M",
    "https://www.youtube.com/watch?v=jFDV4e51Wkc",
    "https://www.youtube.com/watch?v=1cHp7HV8nEA",
    "https://www.youtube.com/watch?v=9OY3R_JUnxc",
    "https://www.youtube.com/watch?v=qqafRNLS1Os",
    "https://www.youtube.com/watch?v=TZf6ZORwO2E",
    "https://www.youtube.com/watch?v=ygqfkgU41X4",
    "https://www.youtube.com/watch?v=zZ4l1a4bItE",
    "https://www.youtube.com/watch?v=LW2UQhMxG7U",
    "https://www.youtube.com/watch?v=UQBD3fF_kKQ",
    "https://www.youtube.com/watch?v=orW3Vwnrszs",
    "https://www.youtube.com/watch?v=SgBDsgU06QQ",
    "https://www.youtube.com/watch?v=uy-z3gIC-Eo",
    "https://www.youtube.com/watch?v=KiYfGY58TXs",
    "https://www.youtube.com/watch?v=5GQSw-TRli4",
    "https://www.youtube.com/watch?v=mlsKhxw-d_Y&t=21s",
    "https://www.youtube.com/watch?v=nRm6aQmkeu8",
    "https://www.youtube.com/watch?v=suVuvgGYkPU",
    "https://www.youtube.com/watch?v=lVB7DxIn9Qs",
    "https://www.youtube.com/watch?v=lhKInyENKtc",
    "https://www.youtube.com/watch?v=Ixlnq4H84N8",
    "https://www.youtube.com/watch?v=Q__fHQfYbvY",
    "https://www.youtube.com/watch?v=1udr2n3nTsc",
    "https://www.youtube.com/watch?v=gVDgMZTVdCo",
    "https://www.youtube.com/watch?v=0LIGIP9vm6g",
    "https://www.youtube.com/watch?v=3DPz6TR7KcQ",
    "https://www.youtube.com/watch?v=dqn7B3rUTUg",
    "https://www.youtube.com/watch?v=lbB5B7_HoQQ",
    "https://www.youtube.com/watch?v=x1JtutI72Qk",
    "https://www.youtube.com/watch?v=N-0DxKGsvGY",
    "https://www.youtube.com/watch?v=0PUFK08i8eM",
    "https://www.youtube.com/watch?v=ZjOnYHmA0jo",
    "https://www.youtube.com/watch?v=H1_InTJGMKs",
    "https://www.youtube.com/watch?v=UlgyBUsaJY8",
    "https://www.youtube.com/watch?v=LHnpkk7cqyU",
    "https://www.youtube.com/watch?v=_qds7IyHBvE",
    "https://www.youtube.com/watch?v=Biimv1SI9JM",
    "https://www.youtube.com/watch?v=UM_lfDRfTMo",
    "https://www.youtube.com/watch?v=JWpsqAvfF0A",
    "https://www.youtube.com/watch?v=ejfBlVsIBKg",
    "https://www.youtube.com/watch?v=792Zt3ZgMmc",
    "https://www.youtube.com/watch?v=bnf-nhB3W0Q",
    "https://www.youtube.com/watch?v=5YghYw0lzNw",
    "https://www.youtube.com/watch?v=yZ7Ma4I7kwo",
    "https://www.youtube.com/watch?v=-fQsJQWdPOk",
    "https://www.youtube.com/watch?v=ihjTSH_TxcE",
    "https://www.youtube.com/watch?v=UsfdM1tJzEk",
    "https://www.youtube.com/watch?v=3QrG8EJzlc4",
    "https://www.youtube.com/watch?v=Q4qmEX2sRgA",
    "https://www.youtube.com/watch?v=WQ_4P1VVgsQ",
    "https://www.youtube.com/watch?v=eS6DpYdgbts",
    "https://www.youtube.com/watch?v=_fRXeqAoIMU",
    "https://www.youtube.com/watch?v=qCmD2mtQJLg",
    "https://www.youtube.com/watch?v=nHFEnIfblIg",
    "https://www.youtube.com/watch?v=vDZE2LT_1eg",
    "https://www.youtube.com/watch?v=T1MehDeMF2Y",
    "https://www.youtube.com/watch?v=CumZDZRH23Q",
    "https://www.youtube.com/watch?v=g6ZRTJyPFFc",
    "https://www.youtube.com/watch?v=0hX-zox6c8I",
    "https://www.youtube.com/watch?v=h95qEZzPZz4",
    "https://www.youtube.com/watch?v=qLigEnxB6Ks",
    "https://www.youtube.com/watch?v=1NQrechTD3o",
    "https://www.youtube.com/watch?v=w-XZq0rjNJo",
    "https://www.youtube.com/watch?v=IjLMDGEBECI",
    "https://www.youtube.com/watch?v=RQGiylNFBIQ",
    "https://www.youtube.com/watch?v=3gylp04jZ1g",
    "https://www.youtube.com/watch?v=7Yo-IENF9Mw",
    "https://www.youtube.com/watch?v=fjjN-5CC_iE",
    "https://www.youtube.com/watch?v=C_Sh8XEmvQg",
    "https://www.youtube.com/watch?v=LJ30DrOPFrc",
    "https://www.youtube.com/watch?v=3KCCBXnV8R0",
    "https://www.youtube.com/watch?v=nWtXFOSqUIo",
    "https://www.youtube.com/watch?v=brwH_Hm4Yb0",
    "https://www.youtube.com/watch?v=LBBzXECtaRc",
    "https://www.youtube.com/watch?v=0t1z6uitxT0",
    "https://www.youtube.com/watch?v=L7zAzrufUJQ",
    "https://www.youtube.com/watch?v=qLUImUXCUw0",
    "https://www.youtube.com/watch?v=aNP5TpyF0rU",
    "https://www.youtube.com/watch?v=j5AzXsr6VF8",
    "https://www.youtube.com/watch?v=vDZE2LT_1eg",
    "https://www.youtube.com/watch?v=cQ_2TxkTnfg"
]

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